# Generated by Django 4.1.7 on 2023-07-31 05:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ARVappApi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Create_Text',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Text_name', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Scene',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('FeaturedtrackerOption', models.CharField(blank=True, max_length=255)),
                ('project_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ARVappApi.createproject')),
            ],
        ),
        migrations.CreateModel(
            name='UploadVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(upload_to='CreateVideoDesign/')),
                ('scene_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productapp.scene')),
            ],
        ),
        migrations.CreateModel(
            name='Video_Transition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transition_enter', models.CharField(blank=True, max_length=255, null=True)),
                ('transition_exit', models.CharField(blank=True, max_length=255, null=True)),
                ('height', models.CharField(blank=True, max_length=255, null=True)),
                ('duration', models.CharField(blank=True, max_length=255, null=True)),
                ('delay', models.CharField(blank=True, max_length=255, null=True)),
                ('video_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productapp.uploadvideo')),
            ],
        ),
        migrations.CreateModel(
            name='Video_Transform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('width', models.CharField(blank=True, max_length=255, null=True)),
                ('height', models.CharField(blank=True, max_length=255, null=True)),
                ('depth', models.CharField(blank=True, max_length=255, null=True)),
                ('position_x', models.CharField(blank=True, max_length=255, null=True)),
                ('position_y', models.CharField(blank=True, max_length=255, null=True)),
                ('position_d', models.CharField(blank=True, max_length=255, null=True)),
                ('Rotation_x', models.CharField(blank=True, max_length=255, null=True)),
                ('Rotation_y', models.CharField(blank=True, max_length=255, null=True)),
                ('Rotation_z', models.CharField(blank=True, max_length=255, null=True)),
                ('Mirror', models.CharField(blank=True, max_length=255, null=True)),
                ('video_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productapp.uploadvideo')),
            ],
        ),
        migrations.CreateModel(
            name='Video_Action',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_action', models.CharField(blank=True, max_length=255, null=True)),
                ('video_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productapp.uploadvideo')),
            ],
        ),
        migrations.CreateModel(
            name='TwoD_ThreeD_Switch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.BooleanField()),
                ('scene_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productapp.scene')),
            ],
        ),
        migrations.CreateModel(
            name='ThreeDModelFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('File', models.FileField(upload_to='ThreeDModelFile/')),
                ('scene_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productapp.scene')),
            ],
        ),
        migrations.CreateModel(
            name='ThreeDModel_Transition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transition_enter', models.CharField(blank=True, max_length=255, null=True)),
                ('transition_exit', models.CharField(blank=True, max_length=255, null=True)),
                ('height', models.CharField(blank=True, max_length=255, null=True)),
                ('duration', models.CharField(blank=True, max_length=255, null=True)),
                ('delay', models.CharField(blank=True, max_length=255, null=True)),
                ('ThreeDModel_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productapp.threedmodelfile')),
            ],
        ),
        migrations.CreateModel(
            name='ThreeDModel_Transform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('width', models.CharField(blank=True, max_length=255, null=True)),
                ('height', models.CharField(blank=True, max_length=255, null=True)),
                ('depth', models.CharField(blank=True, max_length=255, null=True)),
                ('position_x', models.CharField(blank=True, max_length=255, null=True)),
                ('position_y', models.CharField(blank=True, max_length=255, null=True)),
                ('position_d', models.CharField(blank=True, max_length=255, null=True)),
                ('Rotation_x', models.CharField(blank=True, max_length=255, null=True)),
                ('Rotation_y', models.CharField(blank=True, max_length=255, null=True)),
                ('Rotation_z', models.CharField(blank=True, max_length=255, null=True)),
                ('Mirror', models.CharField(blank=True, max_length=255, null=True)),
                ('ThreeDModel_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productapp.threedmodelfile')),
            ],
        ),
        migrations.CreateModel(
            name='ThreeDModel_Action',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.CharField(blank=True, max_length=255, null=True)),
                ('ThreeDModel_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productapp.threedmodelfile')),
            ],
        ),
        migrations.CreateModel(
            name='Text_Transition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transition_enter', models.CharField(blank=True, max_length=255, null=True)),
                ('transition_exit', models.CharField(blank=True, max_length=255, null=True)),
                ('height', models.CharField(blank=True, max_length=255, null=True)),
                ('duration', models.CharField(blank=True, max_length=255, null=True)),
                ('delay', models.CharField(blank=True, max_length=255, null=True)),
                ('text_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productapp.create_text')),
            ],
        ),
        migrations.CreateModel(
            name='Text_Transform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('width', models.CharField(blank=True, max_length=255, null=True)),
                ('height', models.CharField(blank=True, max_length=255, null=True)),
                ('depth', models.CharField(blank=True, max_length=255, null=True)),
                ('position_x', models.CharField(blank=True, max_length=255, null=True)),
                ('position_y', models.CharField(blank=True, max_length=255, null=True)),
                ('position_d', models.CharField(blank=True, max_length=255, null=True)),
                ('Rotation_x', models.CharField(blank=True, max_length=255, null=True)),
                ('Rotation_y', models.CharField(blank=True, max_length=255, null=True)),
                ('Rotation_z', models.CharField(blank=True, max_length=255, null=True)),
                ('Mirror', models.CharField(blank=True, max_length=255, null=True)),
                ('text_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productapp.create_text')),
            ],
        ),
        migrations.CreateModel(
            name='Text_Text',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(blank=True, max_length=255, null=True)),
                ('text_size', models.CharField(blank=True, max_length=255, null=True)),
                ('text_font', models.CharField(blank=True, max_length=255, null=True)),
                ('link', models.CharField(blank=True, max_length=255, null=True)),
                ('text_color', models.CharField(blank=True, max_length=255, null=True)),
                ('alignment', models.CharField(blank=True, max_length=255, null=True)),
                ('text_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productapp.create_text')),
            ],
        ),
        migrations.CreateModel(
            name='Text_Action',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_action', models.CharField(blank=True, max_length=255, null=True)),
                ('text_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productapp.create_text')),
            ],
        ),
        migrations.CreateModel(
            name='Scene_Transition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transition_enter', models.CharField(blank=True, max_length=255, null=True)),
                ('transition_exit', models.CharField(blank=True, max_length=255, null=True)),
                ('height', models.CharField(blank=True, max_length=255, null=True)),
                ('duration', models.CharField(blank=True, max_length=255, null=True)),
                ('delay', models.CharField(blank=True, max_length=255, null=True)),
                ('scene_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productapp.scene')),
            ],
        ),
        migrations.CreateModel(
            name='Scene_PhotoUI',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo_ui', models.BooleanField()),
                ('scene_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productapp.scene')),
            ],
        ),
        migrations.CreateModel(
            name='Project_Content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('target_image', models.ImageField(blank=True, null=True, upload_to='targetimage/')),
                ('opacity', models.CharField(blank=True, max_length=255, null=True)),
                ('orientation', models.CharField(blank=True, max_length=255, null=True)),
                ('dimensions_w', models.CharField(blank=True, max_length=255, null=True)),
                ('dimensions_h', models.CharField(blank=True, max_length=255, null=True)),
                ('units', models.CharField(blank=True, max_length=255, null=True)),
                ('project_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ARVappApi.createproject')),
            ],
        ),
        migrations.CreateModel(
            name='ImageDesign',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='CreateImageDesign/')),
                ('scene_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productapp.scene')),
            ],
        ),
        migrations.CreateModel(
            name='Image_Transition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transition_enter', models.CharField(blank=True, max_length=255, null=True)),
                ('transition_exit', models.CharField(blank=True, max_length=255, null=True)),
                ('height', models.CharField(blank=True, max_length=255, null=True)),
                ('duration', models.CharField(blank=True, max_length=255, null=True)),
                ('delay', models.CharField(blank=True, max_length=255, null=True)),
                ('image_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productapp.imagedesign')),
            ],
        ),
        migrations.CreateModel(
            name='Image_Transform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('width', models.CharField(blank=True, max_length=255, null=True)),
                ('height', models.CharField(blank=True, max_length=255, null=True)),
                ('depth', models.CharField(blank=True, max_length=255, null=True)),
                ('position_x', models.CharField(blank=True, max_length=255, null=True)),
                ('position_y', models.CharField(blank=True, max_length=255, null=True)),
                ('position_d', models.CharField(blank=True, max_length=255, null=True)),
                ('Rotation_x', models.CharField(blank=True, max_length=255, null=True)),
                ('Rotation_y', models.CharField(blank=True, max_length=255, null=True)),
                ('Rotation_z', models.CharField(blank=True, max_length=255, null=True)),
                ('Mirror', models.CharField(blank=True, max_length=255, null=True)),
                ('image_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productapp.imagedesign')),
            ],
        ),
        migrations.CreateModel(
            name='Image_Appearance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('frame_type', models.CharField(blank=True, max_length=255, null=True)),
                ('opacity', models.CharField(blank=True, max_length=255, null=True)),
                ('corner_radius', models.CharField(blank=True, max_length=255, null=True)),
                ('border_width', models.CharField(blank=True, max_length=255, null=True)),
                ('border_color', models.CharField(blank=True, max_length=255, null=True)),
                ('image_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productapp.imagedesign')),
            ],
        ),
        migrations.CreateModel(
            name='Image_Action',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_action', models.CharField(blank=True, max_length=255, null=True)),
                ('image_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productapp.imagedesign')),
            ],
        ),
        migrations.AddField(
            model_name='create_text',
            name='scene_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productapp.scene'),
        ),
        migrations.CreateModel(
            name='Create_Button',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Button_name', models.CharField(blank=True, max_length=255, null=True)),
                ('scene_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productapp.scene')),
            ],
        ),
        migrations.CreateModel(
            name='Button_Transition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transition_enter', models.CharField(blank=True, max_length=255, null=True)),
                ('transition_exit', models.CharField(blank=True, max_length=255, null=True)),
                ('height', models.CharField(blank=True, max_length=255, null=True)),
                ('duration', models.CharField(blank=True, max_length=255, null=True)),
                ('delay', models.CharField(blank=True, max_length=255, null=True)),
                ('button_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='button_transition', to='productapp.create_button')),
            ],
        ),
        migrations.CreateModel(
            name='Button_Transform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('width', models.CharField(blank=True, max_length=255, null=True)),
                ('height', models.CharField(blank=True, max_length=255, null=True)),
                ('depth', models.CharField(blank=True, max_length=255, null=True)),
                ('position_x', models.CharField(blank=True, max_length=255, null=True)),
                ('position_y', models.CharField(blank=True, max_length=255, null=True)),
                ('position_d', models.CharField(blank=True, max_length=255, null=True)),
                ('Rotation_x', models.CharField(blank=True, max_length=255, null=True)),
                ('Rotation_y', models.CharField(blank=True, max_length=255, null=True)),
                ('Rotation_z', models.CharField(blank=True, max_length=255, null=True)),
                ('Mirror', models.CharField(blank=True, max_length=255, null=True)),
                ('button_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='button_transform', to='productapp.create_button')),
            ],
        ),
        migrations.CreateModel(
            name='Button_Text',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(blank=True, max_length=255, null=True)),
                ('text_size', models.CharField(blank=True, max_length=255, null=True)),
                ('text_font', models.CharField(blank=True, max_length=255, null=True)),
                ('link', models.CharField(blank=True, max_length=255, null=True)),
                ('text_color', models.CharField(blank=True, max_length=255, null=True)),
                ('alignment', models.CharField(blank=True, max_length=255, null=True)),
                ('button_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='button_text', to='productapp.create_button')),
            ],
        ),
        migrations.CreateModel(
            name='Button_Appearance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('corner_radius', models.CharField(blank=True, max_length=255, null=True)),
                ('fill_Color', models.CharField(blank=True, max_length=255, null=True)),
                ('border_width', models.CharField(blank=True, max_length=255, null=True)),
                ('border_color', models.CharField(blank=True, max_length=255, null=True)),
                ('button_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productapp.create_button')),
            ],
        ),
        migrations.CreateModel(
            name='Button_Action',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('button_action', models.CharField(blank=True, max_length=255, null=True)),
                ('button_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productapp.create_button')),
            ],
        ),
        migrations.CreateModel(
            name='Background_Sound',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('media_file', models.FileField(blank=True, null=True, upload_to='background_sound/')),
                ('project_content_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productapp.project_content')),
            ],
        ),
        migrations.CreateModel(
            name='Analytics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('track_with', models.CharField(blank=True, max_length=255, null=True)),
                ('project_content_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productapp.project_content')),
            ],
        ),
    ]
