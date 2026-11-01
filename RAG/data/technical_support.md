---
title: Soporte Técnico - Base de Conocimiento
department: Technical Support
company: NovaDesk Solutions (empresa ficticia para pruebas)
version: 5.0
last_updated: 2026-10-01
owner: Equipo de Soporte Técnico N2
tags: [soporte técnico, troubleshooting, errores, contraseñas, vpn, integraciones, api]
---

# Soporte Técnico - Base de Conocimiento

Guías de diagnóstico y solución para los problemas técnicos más frecuentes reportados a la mesa de ayuda de NovaDesk Solutions.

## 1. Requisitos del sistema

| Componente | Requisito mínimo | Recomendado |
|------------|------------------|-------------|
| Navegador | Chrome 120, Edge 120, Firefox 121, Safari 17 | Última versión estable |
| Sistema operativo (app de escritorio) | Windows 10 22H2, macOS 13 | Windows 11, macOS 15 |
| App móvil | Android 11, iOS 16 | Android 14, iOS 18 |
| Ancho de banda | 2 Mbps | 10 Mbps |
| RAM (app de escritorio) | 4 GB | 8 GB |

Internet Explorer **no es compatible**.

## 2. Acceso y autenticación

### 2.1 Restablecer contraseña

1. Ir a https://app.novadesk.example/login y hacer clic en **"¿Olvidó su contraseña?"**.
2. Ingresar el correo corporativo.
3. Abrir el enlace recibido; es válido durante **30 minutos**.
4. Crear una nueva contraseña que cumpla la política.

**Política de contraseñas:**
- Mínimo **12 caracteres**.
- Al menos una mayúscula, una minúscula, un número y un símbolo.
- No puede repetir ninguna de las **5 últimas** contraseñas.
- Expira cada **90 días** (configurable por el administrador entre 30 y 365 días, o desactivable si se usa SSO).

### 2.2 Cuenta bloqueada

La cuenta se bloquea tras **5 intentos fallidos** de inicio de sesión en 15 minutos. El bloqueo dura **30 minutos** y se libera automáticamente. Un administrador de la organización puede desbloquearla antes desde **Admin > Usuarios > Desbloquear**.

### 2.3 Autenticación multifactor (MFA)

- Métodos admitidos: aplicación autenticadora (TOTP), llave de seguridad FIDO2 y SMS (SMS no disponible en Enterprise Plus por política de seguridad).
- Si el usuario pierde su dispositivo MFA, puede usar uno de sus **10 códigos de respaldo**.
- Si no tiene códigos, el administrador debe restablecer el MFA. Soporte de NovaDesk **no** puede restablecer el MFA de un usuario sin la aprobación por escrito de un administrador de su organización.

### 2.4 Inicio de sesión único (SSO)

- Protocolos: SAML 2.0 y OpenID Connect.
- Proveedores probados: Microsoft Entra ID, Okta, Google Workspace y Ping Identity.
- Disponible en planes **Empresarial** y **Enterprise Plus**.
- Error común: **"SAML response signature invalid"** → el certificado del IdP expiró o no coincide. Cargar el certificado actualizado en **Admin > Seguridad > SSO**.

## 3. Códigos de error frecuentes

| Código | Mensaje | Causa probable | Solución |
|--------|---------|----------------|----------|
| ND-401 | Sesión no autorizada | Token de sesión expirado (duración: 12 h) | Cerrar sesión y volver a ingresar. |
| ND-403 | Acceso denegado | El usuario no tiene el rol requerido | Solicitar permisos al administrador. |
| ND-408 | Tiempo de espera agotado | Conexión lenta o proxy corporativo | Verificar red; permitir `*.novadesk.example` en el proxy. |
| ND-413 | Archivo demasiado grande | El adjunto supera el límite de **25 MB** | Comprimir el archivo o compartir enlace. |
| ND-429 | Demasiadas solicitudes | Límite de la API excedido | Esperar 60 s y aplicar backoff exponencial. |
| ND-500 | Error interno | Falla del servidor | Reintentar; si persiste más de 10 min, abrir ticket P2. |
| ND-503 | Servicio no disponible | Mantenimiento o incidente | Revisar https://status.novadesk.example |
| ND-1021 | Sincronización fallida | Conflicto de versiones en la app de escritorio | Actualizar la app y ejecutar "Forzar sincronización". |

## 4. Problemas de rendimiento

**Síntoma:** la plataforma carga lento.

Pasos de diagnóstico:
1. Verificar la página de estado para descartar un incidente general.
2. Probar en una ventana de incógnito (descarta extensiones del navegador).
3. Borrar caché y cookies del navegador.
4. Ejecutar la prueba de conectividad en https://app.novadesk.example/diagnostics y adjuntar el resultado al ticket.
5. Si la latencia supera **300 ms**, el problema probablemente es de la red del cliente.

Información que debe incluir el ticket: navegador y versión, hora exacta del problema con zona horaria, captura de pantalla y el **ID de diagnóstico** generado en el paso 4.

## 5. VPN y redes corporativas

- La plataforma requiere acceso saliente por **HTTPS (puerto 443)** y **WebSocket seguro (WSS, puerto 443)**.
- Dominios que deben permitirse en firewall/proxy:
  - `*.novadesk.example`
  - `cdn.novadesk-static.example`
  - `ws.novadesk.example`
- Las VPN con **inspección SSL** pueden romper la conexión WebSocket y causar que las notificaciones en tiempo real no lleguen. Solución: excluir `ws.novadesk.example` de la inspección SSL.
- Rangos IP para listas blancas (allowlist) entrantes de webhooks: `203.0.113.0/24` y `198.51.100.0/24`.

## 6. Correo electrónico y notificaciones

**Los correos de notificación no llegan:**
1. Revisar la carpeta de spam o correo no deseado.
2. Agregar `notifications@novadesk.example` a remitentes seguros.
3. Verificar en **Perfil > Notificaciones** que el canal de correo esté activo.
4. Si la organización usa su propio dominio de envío, confirmar que los registros **SPF, DKIM y DMARC** estén configurados según **Admin > Correo > Dominio personalizado**.

El retraso normal de una notificación por correo es de hasta **2 minutos**.

## 7. API e integraciones

### 7.1 Límites de la API

| Plan | Solicitudes por minuto | Solicitudes por día |
|------|------------------------|---------------------|
| Básico | Sin acceso a la API | — |
| Profesional | 60 | 10.000 |
| Empresarial | 300 | 100.000 |
| Enterprise Plus | 1.000 | Ilimitadas |

### 7.2 Claves de API

- Se generan en **Admin > Desarrolladores > Claves de API**.
- Solo administradores pueden crearlas.
- Una clave se muestra **una sola vez** al crearla; si se pierde, debe generarse una nueva.
- Las claves inactivas durante **180 días** se revocan automáticamente.
- Nunca enviar claves de API en un ticket. Soporte nunca solicitará una clave completa; solo los **últimos 4 caracteres** para identificarla.

### 7.3 Integraciones nativas

- Microsoft Teams, Slack, Jira, Salesforce y ServiceNow.
- Si una integración deja de sincronizar, la causa más común es que el token OAuth fue revocado o expiró. Solución: **Admin > Integraciones > [Integración] > Reconectar**.

## 8. App de escritorio

- Descarga: https://app.novadesk.example/download
- Las actualizaciones se instalan automáticamente al reiniciar la app.
- Ubicación de logs:
  - Windows: `%APPDATA%\NovaDesk\logs`
  - macOS: `~/Library/Logs/NovaDesk`
- Para reinstalar limpiamente: desinstalar, eliminar la carpeta de datos local y volver a instalar.

## 9. Respaldo y recuperación de datos

- Se realizan respaldos automáticos cada **6 horas**, con retención de **35 días**.
- Los elementos eliminados quedan en la **Papelera durante 30 días** y el usuario puede restaurarlos por sí mismo.
- Para restaurar datos eliminados hace más de 30 días (pero menos de 35), se debe abrir un ticket P2. Esta restauración está disponible solo para planes Empresarial y Enterprise Plus.
- Objetivo de punto de recuperación (RPO): **6 horas**. Objetivo de tiempo de recuperación (RTO): **4 horas**.

## 10. Cómo abrir un buen ticket técnico

Incluir siempre:
1. Descripción clara del problema y del resultado esperado.
2. Pasos para reproducirlo.
3. Código de error exacto (por ejemplo, `ND-1021`).
4. Usuarios afectados y desde cuándo ocurre.
5. Capturas de pantalla o video.
6. ID de diagnóstico o logs de la app de escritorio.

Los tickets con esta información se resuelven, en promedio, un **40% más rápido**.
