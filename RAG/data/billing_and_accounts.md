---
title: Facturación y Cuentas
department: Billing & Accounts
company: NovaDesk Solutions (empresa ficticia para pruebas)
version: 2.3
last_updated: 2026-09-15
owner: Equipo de Facturación
tags: [facturación, pagos, reembolsos, cuentas, suscripciones]
---

# Facturación y Cuentas

Este documento describe las políticas de facturación, planes, métodos de pago, reembolsos y gestión de cuentas de NovaDesk Solutions.

## 1. Planes de suscripción

| Plan | Precio mensual (USD) | Precio anual (USD) | Usuarios incluidos | Almacenamiento |
|------|---------------------|--------------------|--------------------|----------------|
| Básico | 19 | 190 | 3 | 50 GB |
| Profesional | 49 | 490 | 10 | 500 GB |
| Empresarial | 129 | 1.290 | 50 | 2 TB |
| Enterprise Plus | Cotización | Cotización | Ilimitados | Ilimitado |

- El pago anual equivale a **2 meses gratis** respecto al pago mensual.
- Cada usuario adicional cuesta **USD 6/mes** en Básico y Profesional, y **USD 4/mes** en Empresarial.
- Los precios no incluyen impuestos locales (IVA, GST, etc.), que se calculan según el país de facturación.

## 2. Ciclo de facturación

- La facturación se realiza el **mismo día del mes** en que se activó la suscripción.
- Si la fecha de activación fue el 29, 30 o 31, y el mes no tiene ese día, se factura el **último día del mes**.
- Las facturas se envían por correo electrónico al contacto de facturación y quedan disponibles en **Portal > Configuración > Facturación > Historial**.
- Las facturas se emiten en formato PDF y, para clientes en Colombia y México, también en XML como factura electrónica.

## 3. Métodos de pago aceptados

1. Tarjeta de crédito o débito (Visa, Mastercard, American Express).
2. Transferencia bancaria (solo planes anuales y Empresarial o superior).
3. PayPal (solo planes Básico y Profesional).
4. Orden de compra (PO) para Enterprise Plus, con condiciones de pago **Net 30**.

No se aceptan pagos en criptomonedas ni cheques.

## 4. Pagos fallidos y suspensión

Cuando un cobro falla, se aplica el siguiente proceso:

| Día | Acción |
|-----|--------|
| Día 0 | Primer intento fallido. Se notifica por correo. |
| Día 3 | Segundo reintento automático. |
| Día 7 | Tercer reintento y aviso de suspensión. |
| Día 14 | La cuenta pasa a **solo lectura**. |
| Día 30 | La cuenta se **suspende**. Los datos se conservan. |
| Día 90 | Los datos se **eliminan de forma permanente**. |

Para reactivar una cuenta suspendida, el cliente debe pagar el saldo pendiente. La reactivación es inmediata tras confirmarse el pago, y no se cobra cargo de reconexión.

## 5. Política de reembolsos

- **Planes mensuales:** no son reembolsables, salvo error de cobro comprobado.
- **Planes anuales:** reembolso completo si se solicita dentro de los **primeros 30 días**. Después de 30 días, reembolso prorrateado de los meses completos no utilizados, menos un cargo administrativo del **10%**.
- **Cobros duplicados:** se reembolsan al 100% en un plazo de **5 a 10 días hábiles**.
- Los reembolsos se devuelven siempre al método de pago original.
- Para solicitar un reembolso, abrir un ticket con la categoría **"Facturación > Reembolso"** e incluir el número de factura (formato `INV-AAAA-NNNNNN`).

## 6. Cambios de plan

- **Upgrade (subir de plan):** se aplica de inmediato. Se cobra la diferencia prorrateada por los días restantes del ciclo.
- **Downgrade (bajar de plan):** se aplica al **inicio del siguiente ciclo**. No genera reembolso del ciclo actual.
- Al bajar de plan, si el uso de almacenamiento supera el límite del nuevo plan, el cliente tiene **15 días** para reducirlo antes de que se bloqueen nuevas cargas.

## 7. Cancelación de la suscripción

- La cancelación se realiza desde **Portal > Configuración > Facturación > Cancelar suscripción**, o solicitándola al equipo de soporte.
- Solo el **Propietario de la cuenta** (Account Owner) puede cancelar.
- El servicio sigue activo hasta el final del período ya pagado.
- Tras la cancelación, los datos se conservan **60 días** y luego se eliminan. El cliente puede exportarlos en ese período.

## 8. Gestión de cuentas

### 8.1 Roles de cuenta

| Rol | Puede ver facturas | Puede cambiar plan | Puede cancelar | Puede gestionar usuarios |
|-----|-------------------|-------------------|----------------|--------------------------|
| Propietario | Sí | Sí | Sí | Sí |
| Administrador de facturación | Sí | Sí | No | No |
| Administrador | No | No | No | Sí |
| Usuario | No | No | No | No |

### 8.2 Transferencia de propiedad

Para transferir la propiedad de la cuenta, el propietario actual debe:
1. Ir a **Configuración > Cuenta > Transferir propiedad**.
2. Seleccionar a un administrador existente como nuevo propietario.
3. Confirmar mediante el código enviado a su correo (válido por **15 minutos**).

Si el propietario ya no está en la empresa, se requiere una carta firmada por un representante legal y verificación de identidad. Este proceso tarda entre **3 y 5 días hábiles**.

### 8.3 Cambio de datos de facturación

Los datos fiscales (razón social, NIT/RFC/Tax ID, dirección) se pueden modificar en cualquier momento. Los cambios aplican **solo a facturas futuras**; no se reemiten facturas anteriores, salvo solicitud expresa dentro de los **30 días** posteriores a su emisión.

## 9. Descuentos

- **Organizaciones sin ánimo de lucro:** 30% de descuento con documentación válida.
- **Instituciones educativas:** 50% de descuento en el plan Profesional.
- **Startups** (menos de 2 años y menos de 20 empleados): 25% durante el primer año.
- Los descuentos no son acumulables.

## 10. Preguntas frecuentes

**¿Por qué me cobraron más de lo esperado?**
Las causas más comunes son: usuarios adicionales agregados durante el ciclo, un upgrade prorrateado o impuestos locales. Revise el detalle en la factura.

**¿Puedo pagar en pesos colombianos o mexicanos?**
Sí. Se aceptan COP, MXN, EUR y USD. La moneda se fija al crear la suscripción y solo puede cambiarse contactando a facturación.

**¿Dónde descargo un certificado de retención o paz y salvo?**
Se solicita mediante un ticket en la categoría "Facturación > Documentos". El plazo de entrega es de 2 días hábiles.

**¿Cuál es el correo de facturación?**
billing@novadesk.example
