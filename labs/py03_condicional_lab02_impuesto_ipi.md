# LABORATORIO

**Tiempo estimado**: 10-15 minutos

**Nivel de dificultad**: Fácil/Medio

**Objetivos**

Familiarizar al estudiante con:

- Utilizar la instrucción if-else para ramificar la ruta de control.
- Construir un programa completo que resuelva problemas simples de la vida real.

**Escenario**

Érase una vez una tierra - una tierra de leche y miel, habitada por gente feliz y próspera. La gente pagaba
impuestos, por supuesto, su felicidad tenía límites. El impuesto más importante, denominado Impuesto Personal de
Ingresos (IPI, para abreviar) tenía que pagarse una vez al año y se evaluó utilizando la siguiente regla:

- Si el ingreso del ciudadano no era superior a 85,528 pesos, el impuesto era igual al 18% del ingreso menos 556
pesos y 2 centavos (esta fue la llamada exención fiscal).

- Si el ingreso era superior a esta cantidad, el impuesto era igual a 14,839 pesos y 2 centavos, más el 32% del
excedente sobre 85,528 pesos.

Tu tarea es escribir una calculadora de impuestos.

- Debe aceptar un valor de punto flotante: el ingreso.
- A continuación, debe imprimir el impuesto calculado,
redondeado a pesos totales. Hay una función llamada round() que hará el redondeo por ti, la encontrarás en el código
de esqueleto del editor.

Nota: Este país feliz nunca devuelve dinero a sus ciudadanos. Si el impuesto calculado es menor que cero,
solo significa que no hay impuesto (el impuesto es igual a cero). Ten esto en cuenta durante tus cálculos.

**Código propuesto**

Observa el código. Solo lee un valor de entrada, por lo que debes completarlo con
algunos cálculos inteligentes.

```python
ingreso = float(input("Ingrese el ingreso anual:"))
# Escribe aquí tu código
```

**Datos de prueba**

Prueba tu código con los datos que hemos proporcionado.

    Entrada de muestra: 10000
    Resultado esperado: El impuesto es: 1244.0 pesos
    
    Entrada de muestra: 100000
    Resultado esperado: El impuesto es: 19470.0 pesos
    
    Entrada de muestra: 1000
    Resultado esperado: El impuesto es: 0.0 pesos
    
    Entrada de muestra: -100
    Resultado esperado: El impuesto es: 0.0 pesos

