#define PY_SSIZE_T_CLEAN
#include <Python.h>


static PyObject *
test(PyObject *self, PyObject *args)
{
  const char *str;

  if (!PyArg_ParseTuple(args, "s", &str))
    return NULL;

  return PyLong_FromLong(128l);
}


static PyMethodDef GoWsgi[] = {
  {"test", test, METH_VARARGS, "stuff"},
  {NULL, NULL, 0, NULL}                 /* Sentinel */
};

static struct PyModuleDef goWsgimodule = {
  PyModuleDef_HEAD_INIT,
  "goWsgi",
  NULL,
  -1,
  GoWsgi
};

PyMODINIT_FUNC
PyInit_goWsgi(void)
{
  return PyModule_Create(&goWsgimodule);
}
