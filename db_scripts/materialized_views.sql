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


create materialized view tiendas_frecuencia as
select a.codigo_tienda, avg(a.frequency),
t.latitude, t.longitude, t.centro_comercial, t.canal
from
(select s.codigo_tienda, s.ciudad_tienda,
count(distinct s.factura) / count(distinct s.codigo_cliente) as frequency
from sales s
where s.factura is not null
and s.codigo_cliente  is not null
and s.fecha_compra >= '2019-9-1'
group by s.codigo_tienda, s.ciudad_tienda ) a
join tiendas t
on t.cod_tienda = a.codigo_tienda
group by a.codigo_tienda, t.latitude, t.longitude, t.centro_comercial, t.canal with no data;
create unique index on tiendas_frecuencia(codigo_tienda);
refresh materialized view tiendas_frecuencia;


create materialized view parallel_plot as
select avg(valor_neto) as valor_neto,
canal, tipo_negocio, edad, saldo, tipo_tejido
from sales
group by canal, tipo_negocio, edad, saldo, tipo_tejido
with no data;
create unique index on parallel_plot(canal, tipo_negocio, edad, saldo, tipo_tejido);
refresh materialized view parallel_plot;

create materialized view count_avg as
select avg(valor_neto) as ventas_promedio, count(valor_neto) as cantidad_compras,
canal, fecha_compra
from sales s2
group by canal, fecha_compra
with no data;
create unique index on count_avg(canal, fecha_compra);
refresh materialized view count_avg;

drop materialized view edad_count_avg;
create materialized view edad_count_avg as
select
s.fecha_compra,
s.edad,
count(s.valor_neto) as cantidad_compras,
avg(s.valor_neto) as ventas_promedio
from sales s
group by s.fecha_compra,s.edad
with no data;
create unique index on edad_count_avg(fecha_compra,edad);
refresh materialized view edad_count_avg;

create materialized view ciudad_tienda_canal
as
select
s.ciudad_tienda,
s.canal,
sum(valor_neto) as volumen_pesos
from sales s
group by s.canal,s.ciudad_tienda with no data;
create unique index on ciudad_tienda_canal(ciudad_tienda,canal);
refresh materialized view ciudad_tienda_canal;




create materialized view ciudad_tienda_sublinea
as
select
s.ciudad_tienda,
s.sublinea,
sum(valor_neto) as volumen_pesos
from sales s
group by s.sublinea,s.ciudad_tienda with no data;
create unique index on ciudad_tienda_sublinea(ciudad_tienda,sublinea);
refresh materialized view ciudad_tienda_sublinea;



create materialized view ciudad_tienda_grupo_articulo
as
select
s.ciudad_tienda,
s.grupo_articulo,
sum(valor_neto) as volumen_pesos
from sales s
group by s.grupo_articulo,s.ciudad_tienda with no data;
create unique index on ciudad_tienda_grupo_articulo(ciudad_tienda,grupo_articulo);
refresh materialized view ciudad_tienda_grupo_articulo;



create materialized view ciudad_tienda_tipo_articulo
as
select
s.ciudad_tienda,
s.tipo_articulo,
sum(valor_neto) as volumen_pesos
from sales s
group by s.tipo_articulo,s.ciudad_tienda with no data;
create unique index on ciudad_tienda_tipo_articulo(ciudad_tienda,tipo_articulo);
refresh materialized view ciudad_tienda_tipo_articulo;


create materialized view ciudad_tienda_tipo_tejido
as
select
s.ciudad_tienda,
s.tipo_tejido,
sum(valor_neto) as volumen_pesos
from sales s
group by s.tipo_tejido,s.ciudad_tienda with no data;
create unique index on ciudad_tienda_tipo_tejido(ciudad_tienda,tipo_tejido);
refresh materialized view ciudad_tienda_tipo_tejido;


create materialized view ciudad_tienda_mes_venta
as
select
s.ciudad_tienda,
s.mes_venta,
sum(valor_neto) as volumen_pesos
from sales s
group by s.mes_venta,s.ciudad_tienda with no data;
create unique index on ciudad_tienda_mes_venta(ciudad_tienda,mes_venta);
refresh materialized view ciudad_tienda_mes_venta;


create materialized view ciudad_tienda_mes_venta
as
select
s.ciudad_tienda,
s.mes_venta,
sum(valor_neto) as volumen_pesos
from sales s
group by s.mes_venta,s.ciudad_tienda with no data;
create unique index on ciudad_tienda_mes_venta(ciudad_tienda,mes_venta);
refresh materialized view ciudad_tienda_mes_venta;


create materialized view ciudad_tienda_saldo
as
select
s.ciudad_tienda,
s.saldo,
sum(valor_neto) as volumen_pesos
from sales s
group by s.saldo,s.ciudad_tienda with no data;
create unique index on ciudad_tienda_saldo(ciudad_tienda,saldo);
refresh materialized view ciudad_tienda_saldo;
