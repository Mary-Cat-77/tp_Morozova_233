# Репозиторий Морозовой Марии, 233 группа
<h3 align="center">Техническое задание №1 (ТЗ1)</h3> 
<br />
<p>Здесь представлен скрипт на bash, который выполняет поставленное задание. Также, данный скрипт представлен в файлах репозитория под названием "bash_script.sh".</p>
<p>В файлах также представлена входная директория, на которой можно протестировать данный скрипт.</p>
<p>Для проверки работоспособности данного скрипта в командной строке рекомендуется ввести следующее: <b>bash bash_script.sh input_dir output_dir</b> , где input_dir и output_dir - названия входной и выходной дирекорий.
</p>
    
```
#!/bin/bash

echo $1
if ! [ -d $1 ]; then
    echo 'No directory'
fi
if ! [ -d $2 ]; then
    mkdir $2
fi
for file in `find $1 -type f -name "*"`
    do 
        if ! [ -f $2/$(basename $file) ]; then
            cp $file $2/ 
        else 
            cp $file $2/new_$(basename $file)
        fi
done
```
