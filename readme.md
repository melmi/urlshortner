# A simple Clean Architecture project in Python

A simple project to bring clean architecture into the Python (and Django) world!

Everybody knows clean architecture. Numerous people used it in Python before. This is my attempt.

![Class Digram](/doc/diagram.drawio.png)

The entire domain layer is organized into the `domain` folder. It has no dependency on Django or any other library.

I tried everything to be *screaming* obvious.

I enjoyed using [punq](https://github.com/bobthemighty/punq) as an IoC container. IMHO it is very well designed and does not force itself into every detail of the project.

It is worth to mention `get_ioc_view()` function which mimics `as_view()` class method, but using IoC for istantiating classes instead of doing it directly.
