# How the command tree works

Running `infobim` with no arguments, `infobim annotation`, or `infobim project --help` each print a different slice of the same tree. None of it is hand-written. There is no central registry file listing commands — the tree is rebuilt on every invocation by scanning the installed package for plugin files and reading one `METADATA` object off each command class.

InfoBIM does not implement this machinery itself. The whole CLI runtime — command discovery, routing, rendering — lives in the `ontobdc` package. InfoBIM only ships its own plugin files (under `infobim/<domain>/plugin/command/`) and a couple of constants (`ROOT_PACKAGE = "infobim"`, `EXECUTABLE = "infobim"`) that tell `ontobdc`'s machinery which package to scan and which executable name to print.

## The plugin convention

Every domain InfoBIM registers — `cli`, `project`, `annotation`, `ifc`, `drawing`, `2d`, `3d`, `context`, `dev`, `run` — is a Python package shaped like this:

```text
src/infobim/<domain>/plugin/command/*.py
```

Any class in one of those files that implements `CliCommandPort` (`ontobdc.cli.domain.port.command`) and declares a class-level `METADATA` is a command, full stop. There is nothing else to register anywhere else.

```python
class AnnotationCreateCommand(CliCommandPort):
    METADATA: CliCommandMetadata = CliCommandMetadata(
        id="annotation_create",
        logical_component="annotation",
        description="Create an annotation of a given type, with a title.",
        arguments=[
            {
                "accepts": ["--title"],
                "valued": True,
                "parameter": "annotation_title",
                "description": "Title of the annotation.",
                "type": "str",
            },
            # ...
        ],
    )

    @staticmethod
    def accepts(args: list[str]) -> bool: ...
    def check(self) -> bool: ...
    def run(self) -> CommandResponse: ...
```

`METADATA` (`CliCommandMetadata`) is the single source of truth both the router and the tree renderer read from:

| Field | Used for |
| --- | --- |
| `id` | Unique key for the command (also how a component's "entry" command is found, see below). |
| `logical_component` | The domain this command belongs to (`"annotation"`, `"project"`, `"cli"`, …) — how `CommandLoader` filters classes. |
| `description` | The grey one-line text printed under each command in the tree. |
| `arguments` | List of flag definitions (`accepts`, `valued`, `optional`, `description`, `parameter`, `type`) — drives both parameter binding and the usage line shown in the tree. |
| `depends_on` | Health checks that must pass before the command is even offered as a dispatch candidate (defaults to requiring an initialized storage root). |
| `interactive` | Marks a command whose response owns the terminal itself (a TUI), which the renderer must not try to render a second time. |

## Discovery: turning files into classes

`CommandLoader` (`ontobdc.shared.adapter.loader.CommandLoader`) does the actual scanning:

1. Resolves the installed `infobim` package directory (works the same whether InfoBIM is installed normally or in editable mode).
2. For a requested component (say `"annotation"`), looks for `infobim/annotation/plugin/command/`.
3. Imports every module inside it and keeps every class that subclasses `CliCommandPort` **and** whose `METADATA.logical_component` actually matches `"annotation"`.

Because the filter is the declared `logical_component`, not the file's location, a command only shows up where its own metadata says it belongs — the folder layout is a discovery convenience, not the source of truth.

## Dispatch: picking the one command that answers

`CliCommandRunAdapter.make()` (`ontobdc.cli.adapter.command`) is what turns `sys.argv` into a running command:

1. Load the `cli` component's commands as the default candidate set.
2. If the first token doesn't start with `-` (e.g. `annotation`, `project`), try loading *that* component's commands instead. If it has any, that becomes the candidate set and the token is dropped from the remaining args.
3. Call the static `accepts(args)` of every remaining candidate.
4. Exactly one `True` wins and gets instantiated. Zero matches or more than one both raise `CliCommandArgumentException` — ambiguity is a bug, never silently resolved.

Nothing outside the command class itself decides what shape of arguments identifies it. `AnnotationCreateCommand.accepts()` requires `args[0] == "annotation"` plus a `--title`; `AnnotationBaseCommand.accepts()` requires just `args == ["annotation"]` or `["annotation", "--help"]`. The router is deliberately dumb — it just asks every candidate "is this you?".

## Rendering: the same discovery, two shapes

`CommandTreeAdapter` + `TerminalTreeAdapter` (`ontobdc.cli.adapter.tree`) build the ASCII tree, in three steps:

1. **Discover** — either scan every domain on disk (`_discover()` with no explicit list), or use a `command_classes` list the caller already filtered to one component.
2. **Describe** — turn each `METADATA` into a plain dict of description + normalized arguments.
3. **Render** — fold that into a two-level trie (component → usage line) and walk it printing `├──`/`└──`, wrapping each grey description line to the real terminal width.

The usage line for each command is built straight from its `arguments`: a flag gets `<value>` appended when `valued`, is wrapped in `{a|b}` when it accepts more than one spelling, and the whole thing is wrapped in `[...]` when `optional`. No command declares any of this by hand — it falls out of the same `arguments` list used for argument binding.

This is why the same mechanism produces different-looking trees:

| Invocation | Command handling it | What it passes to `CommandTreeAdapter` |
| --- | --- | --- |
| `infobim` (no args) or `infobim --help` | `InfoBIMWelcomeCommand` | no `command_classes` → full scan → the complete tree |
| `infobim cli` / `infobim cli --help` | `CliBaseCommand` | `command_classes` pre-filtered to the `cli` component | 
| `infobim annotation` / `infobim annotation --help` | `AnnotationBaseCommand` | `command_classes` pre-filtered to the `annotation` component |

Each domain follows the same pattern: a `<Domain>BaseCommand` whose only job is to call `CommandLoader(component, ...).get_all()` and feed the result into `CommandTreeAdapter` as an explicit list.

One detail worth calling out: `InfoBIMWelcomeCommand` lists itself in its own `EXCLUDED_COMMAND_IDS`. Its entire purpose is to print the tree, so without that self-exclusion it would show up as an entry inside the tree it renders — `CommandTreeAdapter._is_excluded()` checks a command class's own `EXCLUDED_COMMAND_IDS` for exactly this case.

## The consequence

Adding a new command to InfoBIM never touches a router, a registry, or a help file. Drop a class with `METADATA`, `accepts()`, `check()` and `run()` into the right `plugin/command/` folder, and it is simultaneously:

- a dispatch candidate (`CliCommandRunAdapter` will match it),
- a line in the tree (`CommandTreeAdapter` will render it),
- and self-documenting (its own `description` and `arguments` are the only text that ever appears for it).

Because routing and help rendering both read the exact same `METADATA`, there is no path by which the help text can drift from what the command actually accepts — they are the same data, read twice.
