---
title: Servicio y Acuerdos de Nivel de Servicio (SLA)
department: Service Management
company: NovaDesk Solutions (empresa ficticia para pruebas)
version: 4.1
last_updated: 2026-08-30
owner: Gerencia de Servicio
tags: [sla, disponibilidad, prioridades, escalamiento, créditos de servicio]
---

# Servicio y Acuerdos de Nivel de Servicio (SLA)

Este documento define los niveles de servicio, tiempos de respuesta, prioridades, procesos de escalamiento y compensaciones que NovaDesk Solutions ofrece a sus clientes.

## 1. Canales de soporte

| Canal | Básico | Profesional | Empresarial | Enterprise Plus |
|-------|--------|-------------|-------------|-----------------|
| Portal de tickets | Sí | Sí | Sí | Sí |
| Correo electrónico | Sí | Sí | Sí | Sí |
| Chat en vivo | No | Sí | Sí | Sí |
| Teléfono | No | No | Sí | Sí |
| Gerente técnico de cuenta (TAM) | No | No | No | Sí |

- Correo de soporte: support@novadesk.example
- Teléfono (Empresarial y superior): +1 800 555 0142
- Portal: https://support.novadesk.example

## 2. Horario de atención

- **Básico y Profesional:** lunes a viernes, 8:00 a 18:00 (hora local del cliente), excepto festivos.
- **Empresarial:** lunes a sábado, 7:00 a 22:00.
- **Enterprise Plus:** 24x7x365.
- Los incidentes de **Prioridad 1** se atienden 24x7 en los planes Empresarial y Enterprise Plus, sin importar el horario.

## 3. Definición de prioridades

| Prioridad | Nombre | Descripción | Ejemplo |
|-----------|--------|-------------|---------|
| P1 | Crítica | Servicio caído o inutilizable para toda la organización, sin alternativa. | La plataforma no carga para ningún usuario. |
| P2 | Alta | Funcionalidad principal degradada que afecta a muchos usuarios; existe alternativa limitada. | Las notificaciones por correo no se envían. |
| P3 | Media | Problema que afecta a un usuario o a una función secundaria. | Un reporte exporta columnas desordenadas. |
| P4 | Baja | Consultas, solicitudes de información o mejoras. | ¿Cómo configuro un campo personalizado? |

La prioridad la propone el cliente al crear el ticket, pero el agente de soporte puede **reclasificarla** según el impacto real, informando el motivo.

## 4. Tiempos de primera respuesta

| Prioridad | Básico | Profesional | Empresarial | Enterprise Plus |
|-----------|--------|-------------|-------------|-----------------|
| P1 | 8 h hábiles | 4 h | 1 h | 15 min |
| P2 | 24 h hábiles | 8 h | 4 h | 1 h |
| P3 | 48 h hábiles | 24 h | 8 h | 4 h |
| P4 | 5 días hábiles | 3 días hábiles | 2 días hábiles | 1 día hábil |

## 5. Tiempos objetivo de resolución

| Prioridad | Profesional | Empresarial | Enterprise Plus |
|-----------|-------------|-------------|-----------------|
| P1 | 24 h | 8 h | 4 h |
| P2 | 3 días hábiles | 2 días hábiles | 1 día hábil |
| P3 | 10 días hábiles | 5 días hábiles | 3 días hábiles |
| P4 | Sin objetivo | Sin objetivo | 10 días hábiles |

El plan Básico no tiene tiempos objetivo de resolución garantizados. El reloj del SLA se **pausa** mientras el ticket está en estado **"Esperando al cliente"**.

## 6. Disponibilidad garantizada (uptime)

| Plan | Disponibilidad mensual | Tiempo de inactividad máximo aprox. |
|------|------------------------|-------------------------------------|
| Básico | 99,0% | 7 h 18 min |
| Profesional | 99,5% | 3 h 39 min |
| Empresarial | 99,9% | 43 min |
| Enterprise Plus | 99,95% | 21 min |

La disponibilidad se mide mensualmente en la página de estado: https://status.novadesk.example

### 6.1 Exclusiones

No cuentan como inactividad:
- Mantenimientos programados notificados con al menos **72 horas** de anticipación.
- Ventanas de mantenimiento estándar: **domingos de 2:00 a 5:00 UTC**.
- Fallas causadas por el cliente, sus integraciones o su red.
- Eventos de fuerza mayor.
- Funciones marcadas como **Beta** o **Vista previa**.

## 7. Créditos de servicio

Si no se cumple la disponibilidad mensual, el cliente puede solicitar créditos:

| Disponibilidad real | Crédito (% de la cuota mensual) |
|---------------------|--------------------------------|
| Menor al SLA pero ≥ 99,0% | 10% |
| Entre 98,0% y 98,99% | 25% |
| Entre 95,0% y 97,99% | 50% |
| Menor a 95,0% | 100% |

Condiciones:
- Los créditos deben solicitarse dentro de los **30 días** siguientes al cierre del mes afectado.
- Se aplican como descuento en la siguiente factura; **no se pagan en efectivo**.
- El crédito máximo en un mes es el **100% de la cuota mensual**.
- El plan Básico no es elegible para créditos de servicio.

## 8. Proceso de escalamiento

### 8.1 Escalamiento funcional (técnico)

1. **Nivel 1 (N1):** Mesa de ayuda. Diagnóstico inicial, preguntas frecuentes, restablecimiento de contraseñas.
2. **Nivel 2 (N2):** Especialistas de producto. Problemas de configuración, integraciones y errores reproducibles.
3. **Nivel 3 (N3):** Ingeniería. Bugs de código, incidentes de infraestructura y análisis de causa raíz.

Un ticket P1 se escala automáticamente a N2 a los **30 minutos** si no tiene diagnóstico, y a N3 a las **2 horas**.

### 8.2 Escalamiento jerárquico

Si el cliente no está satisfecho con la atención, puede solicitar escalamiento:

| Nivel | Contacto | Cuándo |
|-------|----------|--------|
| 1 | Líder de turno | En cualquier momento |
| 2 | Gerente de Soporte | Si no hay respuesta del líder en 4 h |
| 3 | Director de Servicio al Cliente | Si el SLA ya fue incumplido |

Correo de escalamiento: escalations@novadesk.example

## 9. Ciclo de vida del ticket

Estados posibles: **Nuevo → Asignado → En progreso → Esperando al cliente → Resuelto → Cerrado**.

- Un ticket en **"Esperando al cliente"** sin respuesta durante **7 días** se marca como Resuelto automáticamente, con dos recordatorios previos (días 3 y 5).
- Un ticket **Resuelto** se cierra automáticamente a los **5 días** si el cliente no lo reabre.
- Un ticket **Cerrado** no puede reabrirse; se debe crear uno nuevo referenciando el número anterior (formato `TCK-NNNNNNN`).

## 10. Encuestas de satisfacción

Al resolver cada ticket se envía una encuesta CSAT de 1 a 5. La meta corporativa es un **CSAT ≥ 4,5** y un **NPS trimestral ≥ 40**. Las calificaciones de 1 o 2 generan una revisión obligatoria por parte del líder de turno en un máximo de **48 horas**.

## 11. Comunicación de incidentes mayores

Durante un incidente P1 que afecte a varios clientes:
- Se publica un aviso en la página de estado en máximo **15 minutos**.
- Se envían actualizaciones cada **30 minutos** hasta la resolución.
- Se entrega un informe de causa raíz (RCA) en un plazo de **5 días hábiles** a clientes Empresarial y Enterprise Plus.
