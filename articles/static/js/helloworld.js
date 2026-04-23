var groupmates = [
    {
        "name": "Александр",
        "surname": "Иванов",
        "group": "БВТ1702",
        "marks": [4, 3, 5]
    },
    {
        "name": "Иван",
        "surname": "Петров",
        "group": "БСТ1702",
        "marks": [4, 4, 4]
    },
    {
        "name": "Кирилл",
        "surname": "Смирнов",
        "group": "БАП1801",
        "marks": [5, 5, 5]
    },
    {
        "name": "Елена",
        "surname": "Козлова",
        "group": "БВТ1702",
        "marks": [5, 4, 5]
    },
    {
        "name": "Дмитрий",
        "surname": "Новиков",
        "group": "БСТ1702",
        "marks": [3, 4, 4]
    }
];

var rpad = function(str, length) {
    str = str.toString();
    while (str.length < length)
        str = str + ' ';
    return str;
};

var printStudents = function(students) {
    console.log(
        rpad("Имя", 15),
        rpad("Фамилия", 15),
        rpad("Группа", 8),
        rpad("Оценки", 20)
    );
    for (var i = 0; i < students.length; i++) {
        console.log(
            rpad(students[i]['name'], 15),
            rpad(students[i]['surname'], 15),
            rpad(students[i]['group'], 8),
            rpad(students[i]['marks'].join(', '), 20)
        );
    }
    console.log('\n');
};

// Фильтрация по группе (ввод с клавиатуры)
var filterByGroup = function() {
    var targetGroup = prompt("Введите название группы для фильтрации (например, БВТ1702):");
    if (targetGroup) {
        var filtered = groupmates.filter(function(student) {
            return student['group'] === targetGroup;
        });
        console.log("Студенты группы " + targetGroup + ":");
        printStudents(filtered);
    } else {
        console.log("Фильтрация отменена.");
    }
};

var averageMark = function(marks) {
    var sum = 0;
    for (var i = 0; i < marks.length; i++) {
        sum += marks[i];
    }
    return sum / marks.length;
};

var filterByAverage = function() {
    var threshold = parseFloat(prompt("Введите минимальный средний балл:"));
    if (!isNaN(threshold)) {
        var filtered = groupmates.filter(function(student) {
            return averageMark(student['marks']) > threshold;
        });
        console.log("Студенты со средним баллом выше " + threshold + ":");
        printStudents(filtered);
    } else {
        console.log("Некорректный ввод.");
    }
};

console.log("=== Все студенты ===");
printStudents(groupmates);

filterByGroup();
//filterByAverage();