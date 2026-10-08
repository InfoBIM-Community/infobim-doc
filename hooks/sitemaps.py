"""Expose the multilingual sitemap at each localized page URL for Material."""

from pathlib import Path
from shutil import copyfile

from mkdocs.config.defaults import MkDocsConfig
from mkdocs.plugins import event_priority


@event_priority(-200)
def on_post_build(config: MkDocsConfig) -> None:
    if config.plugins["i18n"].building:
        return
    site: Path = Path(config.site_dir)
    source: Path = site / "sitemap.xml"
    for page in site.rglob("index.html"):
        destination: Path = page.parent / "sitemap.xml"
        if destination != source and not destination.exists():
            copyfile(source, destination)
