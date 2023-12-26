<!DOCTYPE html>
<html>
<head>
    <title>States</title>
</head>
<body>
    <h1>States</h1>
    <ul>
        {% for state in states %}
        <li>{{ state.id }}: <b>{{ state.name }}</b>
        <ul>
        {% for city in state %}
        <li>{{ city.id }}: <b>{{ city.name }}</b></li>

        {% endfor %}
        </ul>
        </li>
        {% endfor %}
    </ul>
</body>
</html>

