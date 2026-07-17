

IC-1803 Taller de Programación   Profesores Cristian Campos
Instituto Tecnológico de Costa Rica
Ingeniería en Computación
Taller de Programación
## Semestre 2, 2022
## Profesores: Ings. Cristian Campos A
## Proyecto Programado #3
Sistema de ventas

## 1. Introducción

La mayoría de los negocios necesitan una aplicación que les administre su inventario y facturación,
el objetivo de este proyecto es de que el estudiante conozca el proceso que toda empresa maneja,
es decir desde la compra de productos a través de órdenes de compra y la venta de estos a sus
clientes.
- ¿Qué se busca con este proyecto?
El objetivo general de este proyecto es introducir al estudiante en el desarrollo de aplicaciones,
mediante la creación un programa de apoyo empresarial, utilizando las técnicas y herramientas
de programación aprendidas en el curso.
Específicamente se busca lo siguiente:
## 1.
Practicar las habilidades de aplicaciones de software.
- Ejercitar la toma de decisiones sobre el dominio del problema y de la solución.
- Aplicar los conceptos de programación orientado a objetos.
- Manejo de componentes para el uso de interfaz gráfica.
- Estimular la investigación para alcanzar los requerimientos del presente proyecto
- Proyecto por desarrollar
La aplicación debe cumplir con las siguientes especificaciones:
a) Interfaz Gráfica de Usuario (GUI)
Debe permitir una interacción amigable, sencilla e intuitiva entre la aplicación de modo que el
usuario sepa guiarse durante el uso de la aplicación

IC-1803 Taller de Programación   Profesores Cristian Campos
b) Control de acceso
La aplicación contará con una pantalla donde solicitará un nombre de usuario y contraseña, esto
para ingresar a los módulos necesarios para el uso de este programa. Para esto debe existir un
archivo  donde  se  almacene  el  nombre  completo  de  la persona,  usuario  y  contraseña,  por
ejemplo:
ccampos; abc123;
c) Pantalla principal
Debe contar con un menú con la siguiente organización:
## • Administración
o Categorías
o Productos
o Clientes
o Proveedores
- Punto de venta
o Facturación
o Orden de compra
o Búsquedas de facturas
## • Salir
d) Categorías
En  este módulo  el  usuario  podrá  crear,  modificar, listar y  borrar  categorías. Los  datos  por
guardar son su código y el nombre. El código debe ser numérico y auto incrementable. No se
podrá borrar una categoría cuyo producto asociado a este ya haya sido facturado. Para buscar
un cliente deberá hacerse por su código.
e) Productos
En  este  módulo  el  usuario  podrá crear,  modificar, listar  y  borrar  productos. Los  datos  por
guardar son su código, nombre del producto, código de categoría, cantidad y precio unitario
de venta. El código del producto debe ser numérico y auto incrementable. No se podrá borrar
un producto que haya sido facturado además cada vez que este se facture debe disminuir su
cantidad, no puede existir valores negativos y no se podrá facturar cuando la cantidad sea
menor a la cantidad facturada. Debe existir una ventana para buscar un producto ya sea para
ser modificado o borrado, debe poder buscarse por su categoría y/o su código.  Al momento
de crearse un nuevo producto, su cantidad por defecto será CERO.
f) Clientes
En este módulo el usuario podrá crear, modificar, listar y borrar clientes. Los datos por guardar
son su código, nombre del cliente (nombre y sus dos apellidos), teléfono y correo electrónico.
El código debe ser numérico y auto incrementable. No se podrá borrar un cliente que haya sido
facturado. Para buscar un cliente deberá hacerse por su cédula

IC-1803 Taller de Programación   Profesores Cristian Campos
g) Proveedores
En este módulo el usuario podrá crear, modificar, listar y borrar proveedores. Los datos por
guardar son su código, nombre del proveedor (nombre y sus dos apellidos), teléfono y correo
electrónico.  El código  debe  ser  numérico  y  auto  incrementable.  No  se  podrá  borrar  un
proveedor  que  haya  sido  creado  una  orden  de  compra. Para  buscar  un  proveedor  deberá
hacerse por su cédula.
h) Órdenes de compra
Cuando se crea un producto, por defecto este tendrá una cantidad (inventario) de CERO, para
agregar unidades a su inventario, es necesario realizar una orden de compra.
En este módulo el usuario podrá crear, listar y anular órdenes de compra. Los datos por guardar
son su código de la orden de compra, código del proveedor, fecha y Total. El código debe ser
numérico y auto incrementable. Para el detalle de la orden de compra será necesario, código
de la orden de compra, código del producto, cantidad y precio unitario. El total de la orden de
compra debe ser calculado según suma del detalle de sus productos. Para poder buscar un
orden de compra será a través de su número de orden
Ejemplo consultar orden de compra:
Orden de compra #50
Proveedor: FENSA
## Fecha: 10/12/2020
Producto Cantidad    Precio unitario Total
## 05 Coca Cola 2ltrs 100 600 60,000
## 06 Tropical Te Frio 2lts 100 500 50,000
## Total 110,000
Se podrá anular una orden siempre y cuando no genere un inventario en negativo.
i) Facturación (Ventas)
En este módulo el usuario podrá crear y anular facturas para la venta de los productos. Los datos
por guardar son su código de la factura, código del cliente, fecha y total. El código debe ser
numérico y auto incrementable. Para el detalle de la facturación será necesario, código de la
factura, código del producto, cantidad y precio unitario. El total de la factura debe ser calculado

IC-1803 Taller de Programación   Profesores Cristian Campos
según suma del detalle de sus productos. Se podrá anular una factura, al hacerse esto, debe
sumarse estas cantidades en el inventario del producto que se facturó. Para poder buscar una
factura será a través de su número.
Ejemplo de consultar factura:
## Factura #18
## Cliente: Cristian Campos
## Fecha: 10/12/2020
Producto Cantidad    Precio unitario Total
## 15 Coca Cola 2ltrs 2 1,200 2,400
## 16 Tropical Te Frio 2lts 1 850 850
## Total 3,280
## 4. Puntos Extra
Se otorgarán 15 puntos extras al estudiante que logre implementar los siguientes reportes en
formato pdf:
- Factura: dado un número de factura válido generar el documento respectivo
- Lista de facturas, este documento debe contener, el número de factura, el nombre del
producto, cantidad, precio unitario y precio total. Al final del documento el total de
todo lo facturado (vendido)
- Lista de órdenes de compra, este documento debe contener, el número de la orden de
compra, el nombre del producto, cantidad, precio unitario y precio total. Al final del
documento el total de todo lo comprado
Cada reporte vale 5 puntos
- Aspectos técnicos
El proyecto deberá estar escrito en el lenguaje de programación Python y se deben desarrollar
las funcionalidades de usuario por medio de interfaz gráfica (Tkinter).
Además, debe considerar lo siguiente:

- Se deben manejar mensajes claros al usuario.
- Realizar validaciones de captura de campos.

IC-1803 Taller de Programación   Profesores Cristian Campos
- Toda función bult-in de Python que deseen utilizar debe ser validada con el profesor
(no incluye las relacionadas a interfaz).
- En el desarrollo del programa se deberá utilizar Programación Orientada a Objetos.
- Se considerará en la evaluación el aprovechamiento del tiempo dado al desarrollo del
proyecto.
- Deben utilizar nombres de variables, argumentos y funciones significativas.
## 6. Documentación

El código fuente debe tener documentación interna, con comentarios precisos y bien ubicados.
Cada función debe tener descripción, nombre, entradas, salidas y restricciones.
La  documentación  es  un  aspecto  de  gran  importancia  en  el  desarrollo  de  programas,
especialmente en tareas relacionadas con el mantenimiento de estos.
Para la documentación interna, deberán incluir comentarios descriptivos para cada función,
con sus entradas, salidas, restricciones y objetivo.
La documentación externa deberá incluir:

## 1.
## Portada.
- Tabla de contenidos.
- Manual de usuario: instrucciones de compilación, ejecución y uso.
- Pruebas de funcionalidad: Enlace del video (youtube) donde se demuestre el uso de la
aplicación
- Diseño del programa: descripción de las clases creadas
- Librerías usadas: creación de archivos, etc.
## 7.
Análisis de resultados: objetivos alcanzados, objetivos no alcanzados, y razones por las
cuales no se alcanzaron los objetivos (en caso de haberlos).
## 8. Conclusión (es)
## 7. Evaluación

La evaluación se va a centrar en dos elementos: programación y documentación. El proyecto
programado tiene un valor de 25% de la nota final, en el rubro de Proyectos.

Desglose de la evaluación del proyecto programado:

## 1.
Documentación interna 5 ptos.
- Documentación externa 10 ptos.
- Funcionalidad 75 ptos (ver detalle en Software a Desarrollar)
- Revisión del proyecto (según desenvolvimiento en la entrevista) 10 ptos

IC-1803 Taller de Programación   Profesores Cristian Campos
- Forma de trabajo

El trabajo se debe realizar en equipos de 2 personas.
- Aspectos administrativos

Subir el proyecto al repositorio (https://classroom.github.com/a/YqGXgapf ) y que contenga 2
carpetas llamadas documentación y programa, en la primera deberá incluir el documento en
formato pdf , y en la segunda los archivos y/o carpetas necesarias para la implementación de
esta tarea. El archivo info.txt debe contener la siguiente información (cualidades):
a. Nombre del curso
b. Número de semestre y año lectivo
c. Nombre del Estudiante
d. Número de carné del estudiante
e. Número del proyecto programado
f. Fecha de entrega
g. Estatus  de  la  entrega  (debe  ser CONGRUENTE  con  la  solución  entregada):
[Deplorable|Regular|Buena|MuyBuena|Excelente|Superior
## 1
## ]
## 10. Entrega

La fecha de entrega del proyecto será el domingo 27 de noviembre a las 11pm. Después de
este punto, NO SE ACEPTARÁN más trabajos.
## 11. Referencias
- http://acodigo.blogspot.com/p/python.html
- http://acodigo.blogspot.com/2017/03/tkinter-grid.html
- https://python-para-impacientes.blogspot.com/2015/12/tkinter-disenando-ventanas-
graficas.html
- https://www.blog.pythonlibrary.org/2018/06/05/creating-pdfs-with-pyfpdf-and-python/
- https://towardsdatascience.com/creating-pdf-files-with-python-ad3ccadfae0f


## 1
Solo si incluye los puntos extras