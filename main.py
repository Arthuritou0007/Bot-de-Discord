import discord
import os
from dotenv import load_dotenv

# 1. Cargar las variables secretas del archivo .env
load_dotenv()
TOKEN = os.getenv('TOKEN_DISCORD')

# 2. Configurar los permisos (intents)
intents = discord.Intents.default()
# Habilitamos el intent de lectura para cuando hagamos el bot de "Gay el de abajo"
intents.message_content = True 

# 3. Crear el cliente del bot
cliente = discord.Client(intents=intents)

# 4. El sensor de encendido (Evento on_ready)
@cliente.event
async def on_ready():
    print(f'¡Estatus: Conectado exitosamente como {cliente.user}!')
    print('El 1% de hoy está completado. 🚀')

@cliente.event
async def on_message(mensaje):
    if mensaje.content == "Gay el de abajo":
        await mensaje.channel.send("o sea el diablo")

# 5. Encender el bot usando la variable oculta
cliente.run(TOKEN)