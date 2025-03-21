# Generated by Django 5.1.7 on 2025-03-20 08:13

import django.contrib.postgres.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
                ('month', models.CharField(choices=[('january', 'Январь'), ('february', 'Февраль'), ('march', 'Март'), ('april', 'Апрель'), ('may', 'Май'), ('june', 'Июнь'), ('july', 'Июль'), ('august', 'Август'), ('september', 'Сентябрь'), ('october', 'Октябрь'), ('november', 'Ноябрь'), ('december', 'Декабрь')], max_length=16)),
                ('day', models.IntegerField()),
                ('protocol_number', models.IntegerField()),
                ('meeting_type', models.CharField(choices=[('regular', 'Очередное'), ('emergency', 'Чрезвычайное'), ('extra', 'Экстренное'), ('ongoing', 'Продолженное')], max_length=16)),
                ('deputies', models.IntegerField()),
                ('presiding', models.CharField(max_length=64)),
                ('quorum', models.BooleanField()),
                ('position_1870', models.CharField(choices=[('А)', 'Дела по устройству и управления городским хозяйством; дела по устройству и управления городским хозяйством.'), ('Б)', 'Дела по внешнему благоустройству города: водопровод, предосторожности против пожаров, предупреждения скотских падежей, охрана порядка в общественных местах.'), ('В)', 'Продовольствие, торговля, здравоохранение, меры предосторожности против пожаров промышленность, устройство пристаней, бирж и кредитных учреждений.'), ('Г)', 'Устройство за счет города благотворительных заведений и больниц, образование, а также театры, библиотеки, музеи.'), ('Д)', 'Подача ходатайств.'), ('Е)', 'Другие обязанности.')], max_length=2)),
                ('position_1892', models.CharField(choices=[('I', 'Заведование установленными в пользу городских поселений сборами и повинностями.'), ('II', 'Заведование капиталами и другими имуществами городского поселения.'), ('III', 'Попечение об устранении недостатка продовольственных средств способами, имеющимися для сего в распоряжении общественного управления.'), ('IV', 'Содержание в исправности и устройстве состоящих в ведении общественного управления улиц, площадей, мостовых, набережных, пристаней, бечевников, тротуаров, общественных садов, бульваров, водопроводов, сточных труб, каналов, прудов, канав, мостов, гатей и переправ, а также освещения городского поселения.'), ('V', 'Попечение о призрении бедных и о прекращении нищенства; устройство благотворительных и лечебных заведений и заведование ими на одинаковых с земскими учреждениями основаниях.'), ('VI', 'Участие в мероприятиях по охранению народного здравия и предупреждению и пресечению продажей скота, развитие средств врачебной помощи городскому населению и изыскание способов к улучшению местных условий в санитарном отношении.'), ('VII', 'Попечение о лучшем устройстве городского поселения по утвержденным планам, а также о мерах предосторожности против пожаров и других бедствий.'), ('VIII', 'Участие в заведовании взаимным страхованием городских имуществ от огня.'), ('IX', 'Попечение о развитии средств народного образования и установленное законом участие в заведовании учебными заведениями.'), ('X', 'Попечение об устройстве общественных библиотек, музеев, театров и других подобного рода общеполезных учреждений.'), ('XI', 'Воспособление зависящими от общественного управления способами развитию местной торговли и промышленности, устройство рынков и базаров, надзор за правильным производством торговли, устройство кредитных учреждений по правилам Устава Кредитного, а равно содействие устройству биржевых учреждений.'), ('XII', 'Удовлетворение возложенных в установленном порядке, на общественное управление потребности воинского и гражданского управлений.'), ('XIII', 'Дела, предоставленные ведению общественного управления на основании особых законоположений и Уставов.')], max_length=5)),
                ('author_classification', models.CharField(choices=[('finance', 'Финансы'), ('food', 'Продовольствие'), ('improvement', 'Благоустройство'), ('transport', 'Транспорт'), ('charity', 'Благотворительность'), ('health_care', 'Здравоохранение'), ('city_government', 'Городское управление'), ('construction', 'Строительство'), ('education', 'Образование'), ('culture', 'Культура'), ('industry', 'Промышленность'), ('trading', 'Торговля'), ('legal', 'Юридический')], max_length=16)),
                ('author_classification_2', models.CharField(blank=True, choices=[('finance', 'Финансы'), ('food', 'Продовольствие'), ('improvement', 'Благоустройство'), ('transport', 'Транспорт'), ('charity', 'Благотворительность'), ('health_care', 'Здравоохранение'), ('city_government', 'Городское управление'), ('construction', 'Строительство'), ('education', 'Образование'), ('culture', 'Культура'), ('industry', 'Промышленность'), ('trading', 'Торговля'), ('legal', 'Юридический')], max_length=16, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=8)),
                ('description', models.TextField(max_length=1024)),
                ('solution', models.CharField(choices=[('agree', 'Согласны'), ('put_off', 'Отложить'), ('refuse', 'Отказать'), ('take_note', 'Принять к сведению')], max_length=16)),
                ('solution_content', models.TextField(blank=True, max_length=1024)),
                ('case_number', models.CharField(max_length=8)),
                ('sheet_numbers', django.contrib.postgres.fields.ArrayField(base_field=models.DecimalField(decimal_places=1, max_digits=5), size=None)),
                ('meeting', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meetings.meeting')),
            ],
        ),
        migrations.AddField(
            model_name='meeting',
            name='tag',
            field=models.ManyToManyField(to='meetings.tag'),
        ),
    ]
