# Generated by Django 3.2.5 on 2021-09-08 16:23

from django.db import migrations, models
import recipes.models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0006_alter_recipeingredientimage_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipeingredientimage',
            name='image',
            field=models.ImageField(upload_to=recipes.models.recipe_ingredient_image_upload_handler),
        ),
    ]