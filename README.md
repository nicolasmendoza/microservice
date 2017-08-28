Microservicio
===============================

Esta "API" corresponde a un ejercicio de programación, mi idea era proveer un set de endpoints pero finalmente no ha sido posible. La API permite consultar el pronóstico de tiempo por día, el pronóstico corresponde a una galaxia lejana y ficticia.

La "API" es un simple endpoint corriendo sobre la librería Falcon (python), también usa SQLAlchemy y PosgtreSQL como DB. Y por supuesto usa Hidrógeno (https://github.com/nicolasmendoza/hidrogeno), hidrógeno "alimenta" la db. 
Una lástima no haber alcanzado a terminar lo que había planeado para este "Microservice".  

Enjoy!:

Endpoint: http://hidrogeno-ml.herokuapp.com/v1/pronosticos/dia/566

Screencast de hydrogen corriendo en Heroku: https://vimeo.com/231357469

Requerimientos: Python 3.5, Falcon. SqlAlchemy, PostgreSQL, Hidrogeno.

..
```

Uso
===

Consultar pronóstico x día. Ejemplo, día 456
- Request
```shell
curl -GET http://hidrogeno-ml.herokuapp.com/v1/pronosticos/dia/456 -H "Content-Type: application/json"

- Response
```json
{
meta: {
code: 200,
message: "OK"
  },
data: {
wheater: "lluvia",
day: 456,
precipitation: 5450
  }
}
```
