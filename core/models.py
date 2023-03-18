from django.db import models


class Manga(models.Model):
    name = models.CharField(max_length=255)
    popularity_index = models.PositiveIntegerField()
    rating = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Chapter(models.Model):
    number = models.PositiveIntegerField(default=1)
    manga = models.ForeignKey(Manga, on_delete=models.CASCADE, related_name="chapters")


class Page(models.Model):
    page_number = models.PositiveIntegerField()
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, related_name="pages")

    def file_path(instance, filename):
        return f"media/documents/{instance.chapter.id}/{instance.page_number}.png"

    def file_path_colored(instance, filename):
        return f"media/documents/colored/{instance.chapter.id}/{instance.page_number}.png"

    file = models.ImageField(upload_to=file_path)

    colored_file = models.ImageField(upload_to=file_path_colored, blank=True, null=True)
