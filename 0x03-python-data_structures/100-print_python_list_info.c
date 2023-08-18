#include <Python.h>

/**
 * print_python_list_info - prints information about
 * Python object.
 * @p:python object to obtain information about.
 * Return: void
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t size, stored, i;

	stored = ((PyListObject *)p)->allocated;
	size = PyList_Size(p);
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", stored);
	i = 0;
	while (i < size)
	{
		printf("Element %ld: %s\n",
		       idx,
		       (PY_TYPE(PyList_GetItem(p, idx)))->tp_name);
		i = i + 1;
	}
}
