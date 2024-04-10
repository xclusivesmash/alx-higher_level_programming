#include "Python.h"
#include <stdio.h>
#include <string.h>

/**
 * print_python_string - prints information about
 * Python strings.
 * @p: Python object (class) paased to a C function.
 * Return: void.
 */
void print_python_string(PyObject *p)
{
	long int len;
	PyASCIIObject *ll;

	printf("[.] string object info\n");
	/* CHECK FOR INVALID STRING */
	if (strcmp(p->ob_type->tp_name, "str") != 0)
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}
	/* CAST BACK PyObject to original data type */
	ll = (PyASCIIObject *)(p);
	len = ll->length;

	if (PyUnicode_IS_COMPACT_ASCII(p))
		printf("  type: compact ascii\n");
	else
		printf("  type: compact unicode object\n");
	printf("  length: %ld\n", len);
	printf("  value: %ls\n", PyUnicode_AsWideCharString(p, &len));
}
