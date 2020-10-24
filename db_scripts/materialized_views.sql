create materialized view venta_ciudad_tienda as 
select sum(s.valor_neto) / count(distinct s.codigo_tienda) as tienda_x_ciudad, s.ciudad_tienda, s.canal 
from sales s
group by s.ciudad_tienda, s.canal with no data;
create unique index on venta_ciudad_tienda(ciudad_tienda, canal);
refresh materialized view venta_ciudad_tienda;


create materialized view ventas_diarias
as 
select  
fecha_compra,
count(distinct s.factura) as numero_ventas, 
count(s.id_sale) as numero_productos, 
sum(s.valor_neto) as volumen_ventas,
sum(s.valor_neto)/count(distinct s.factura) as promedio_ventas, 
avg(s.valor_neto) as promedio_productos
from sales s
where s.factura is not null
group by s.fecha_compra
with no data;
create unique index on ventas_diarias(fecha_compra);
refresh materialized view ventas_diarias;


create materialized view canal_edad_tipo_ciudad
as
select
s.canal, 
s.edad, 
s.tipo_articulo, 
s.ciudad_tienda,
sum(valor_neto) as volumen_pesos, 
count(id_sale) as cantidad_ventas
from sales s
group by s.canal, s.tipo_articulo, s.edad, s.ciudad_tienda with no data;
create unique index on canal_edad_tipo_ciudad(canal, tipo_articulo, edad, ciudad_tienda);
refresh materialized view canal_edad_tipo_ciudad;