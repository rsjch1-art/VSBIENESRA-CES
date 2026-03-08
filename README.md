# Sitio Web de Bienes Raíces - Miriam Vazquez

Sitio web profesional de bienes raíces con panel de administración completo.

## Características

- ✅ Diseño responsive y moderno
- ✅ Panel de administración con autenticación
- ✅ Gestión completa de propiedades (CRUD)
- ✅ Búsqueda y filtrado avanzado
- ✅ Base de datos SQLite integrada
- ✅ API REST completa

## Tecnologías

- **Backend**: Flask (Python)
- **Base de datos**: SQLite
- **Frontend**: HTML5, CSS3, JavaScript
- **Framework CSS**: Bootstrap 5

## Instalación Local

1. Clona el repositorio
2. Instala las dependencias:
   ```bash
   cd backend
   pip install -r requirements.txt
   ```
3. Ejecuta el servidor:
   ```bash
   python app.py
   ```
4. Abre http://localhost:5000 en tu navegador

## Credenciales de Admin

- **Usuario**: miriam
- **Contraseña**: Miriam*1

## Deployment

### Opción 1: Railway (Recomendado)

1. Crea una cuenta en [Railway.app](https://railway.app)
2. Conecta tu repositorio de GitHub
3. Railway detectará automáticamente la configuración
4. El sitio estará disponible en una URL de Railway

### Opción 2: Heroku

1. Crea una cuenta en [Heroku](https://heroku.com)
2. Instala Heroku CLI
3. Despliega:
   ```bash
   heroku create
   git push heroku main
   ```

### Opción 3: VPS (DigitalOcean, Vultr, etc.)

1. Configura un servidor Ubuntu/Debian
2. Instala Python y Nginx
3. Clona el repositorio
4. Configura Gunicorn como servidor WSGI
5. Configura Nginx como proxy reverso

## Estructura del Proyecto

```
/
├── backend/
│   ├── app.py              # Servidor Flask principal
│   ├── requirements.txt    # Dependencias Python
│   ├── inmobiliaria.db     # Base de datos SQLite
│   └── Procfile           # Configuración para Railway/Heroku
├── frontend/
│   ├── index.html         # Página principal
│   ├── admin.html         # Panel de administración
│   ├── styles.css         # Estilos CSS
│   └── script.js          # JavaScript del frontend
└── img/                   # Imágenes del sitio
```

## API Endpoints

- `GET /` - Página principal
- `GET /admin.html` - Panel de administración
- `POST /api/login` - Login de administrador
- `GET /api/propiedades` - Obtener todas las propiedades
- `POST /api/agregar_propiedad` - Agregar nueva propiedad
- `POST /api/eliminar_propiedad` - Eliminar propiedad
- `POST /api/logout` - Cerrar sesión

## Desarrollo

Para desarrollo local, ejecuta:
```bash
cd backend
python app.py
```

El servidor se reiniciará automáticamente con cambios.

## Contribución

1. Fork el proyecto
2. Crea una rama para tu feature
3. Commit tus cambios
4. Push a la rama
5. Abre un Pull Request

## Licencia

Este proyecto está bajo la Licencia MIT.