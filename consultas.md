# Consultas ORM — Clase 5

## 1. Obtener todos los productos

```python
Producto.objects.all()
```

## 2. Filtrar por nombre

```python
Producto.objects.filter(nombre="Mouse")
```

## 3. Buscar productos con precio mayor a 30000

```python
Producto.objects.filter(precio__gt=30000)
```

## 4. Buscar productos cuyo nombre contenga "remera"

```python
Producto.objects.filter(nombre__icontains="remera")
```

## 5. Buscar productos con precio menor a 30000

```python
Producto.objects.filter(precio__lt=30000)
```

## 6. Buscar varios productos por nombre

```python
Producto.objects.filter(nombre__in=["Mouse", "Teclado", "monitor"])
```

## 7. Excluir un producto

```python
Producto.objects.exclude(nombre="Mouse")
```

## 8. Obtener un producto específico

```python
Producto.objects.get(nombre="Mouse")
```

## 9. Obtener la categoría de un producto

```python
producto.categoria
```

## 10. Obtener los productos de una categoría

```python
categoria.producto_set.all()
```
