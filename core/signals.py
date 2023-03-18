from django.db.models.signals import post_save
from django.dispatch import receiver

from core.manga_colorization.colorizator import MangaColorizator
from core.manga_colorization.inference import colorize_single_image
from core.models import Page


@receiver(post_save, sender=Page)
def colorize_file(sender, instance, created, **kwargs):
    if created:
        device = "cpu"
        colorizer = MangaColorizator(
            device, "core/manga_colorization/networks/generator.zip", "core/manga_colorization/networks/extractor.pth"
        )
        new_image_path = f"{instance.file.path}_colored.png"
        print("colorize start")
        colorize_single_image(instance.file.path, new_image_path, colorizer)
        print("colorize finish")
        instance.colored_file.save(new_image_path, open(new_image_path, "rb"))
        print("saving finish")
