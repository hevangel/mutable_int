#include <Python.h>

// Copy the data value of Python int object
static PyObject* copy_int(PyObject* self, PyObject* args)
{
    int i;
    int ok;
    PyObject * obj0 = 0;
    PyObject * obj1 = 0;

    ok = PyArg_ParseTuple(args, "OO", &obj0, &obj1);
    if (!ok) {
        PyErr_SetString(PyExc_TypeError, "both arguments must be python objects");
        return (PyObject *) NULL;
    };

    if (!PyLong_Check(obj0) || !PyLong_Check(obj1)) {
        PyErr_SetString(PyExc_TypeError, "both arguments must be PyLong type");
        return (PyObject *) NULL;
    };

    PyLongObject * lobj0 = (PyLongObject *)obj0;
    PyVarObject * vobj0 = (PyVarObject *)obj0;
    PyLongObject * lobj1 = (PyLongObject *)obj1;
    PyVarObject * vobj1 = (PyVarObject *)obj1;

    if (vobj1->ob_size == 0) {
        for(i = 0; i < abs(Py_SIZE(obj0)); i++) {
            lobj0->ob_digit[i] = 0;
        }
    } else {
        vobj0->ob_size = vobj1->ob_size;
        for(i = 0; i < abs(Py_SIZE(obj1)); i++) {
            lobj0->ob_digit[i] = lobj1->ob_digit[i];
        }
    }
    
    return Py_None;
}


// Print all the interal fields of Python int object
static PyObject* print_int_info(PyObject* self, PyObject* args)
{
    int ok;
    PyObject * obj0 = 0;

    ok = PyArg_ParseTuple(args, "O", &obj0);
    if (!ok) {
        PyErr_SetString(PyExc_TypeError, "the argument must be python object");
        return (PyObject *) NULL;
    };

    if (!PyLong_Check(obj0)) {
        PyErr_SetString(PyExc_TypeError, "the argument must be PyLong type");
        return (PyObject *) NULL;
    };

    printf("PyLong_Check: %d\n", PyLong_Check(obj0));
    printf("PyLong_AsLong: %ld\n", PyLong_AsLong(obj0));
    PyLongObject * lobj = (PyLongObject *)obj0;
    PyVarObject * vobj = (PyVarObject *)obj0;

    printf("sizeof(PyLongObject): %ld\n", sizeof(PyLongObject));
    printf("sizeof(PyVarObject): %ld\n", sizeof(PyVarObject));
    printf("sizeof(vobj->ob_size): %ld\n", sizeof(vobj->ob_size));

    printf("obj addr: %p\n", obj0);
    printf("ob_size addr: %p\n", &vobj->ob_size);
    printf("ob_digit addr: %p\n", &lobj->ob_digit[0]);
 
    printf("ob_size: %ld\n", Py_SIZE(obj0));
    short abs_ob_size = abs(Py_SIZE(obj0));
    printf("abs(ob_size): %d\n", abs_ob_size);
    short i;
    for(i = 0; i < abs_ob_size; i++) {
        printf("ob_digit[%d]: 0x%x\n", i, lobj->ob_digit[i]);
    }
    
    return Py_None;
}

// Our Module's Function Definition struct
// We require this `NULL` to signal the end of our method
// definition
static PyMethodDef myMethods[] = {
    { "print_int_info", print_int_info, METH_VARARGS, "Print internal fields of int" },
    { "copy_int", copy_int, METH_VARARGS, "Copy raw memory of int" },
    { NULL, NULL, 0, NULL }
};

// Our Module Definition struct
static struct PyModuleDef myModule = {
    PyModuleDef_HEAD_INIT,
    "_mutableint",
    "Mutable Integer package util functions",
    -1,
    myMethods
};

// Initializes our module using our above struct
PyMODINIT_FUNC PyInit__mutableint(void)
{
    return PyModule_Create(&myModule);
}

