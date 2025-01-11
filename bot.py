import discord
from discord.ext import commands


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
  
@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un {bot.user}, Mi objetivo es mostrarte juegos para que te puedas divertir y consejos para mejoarar en ellos!')

@bot.command()
async def Comandos(ctx):
    await ctx.send(f'$hello, $heh, $hacker, $emoji, $Juegos, $Haxball, $Poki, $Juegos friv, $Minijuegos, $Ajedrez, $adios, $noticias')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def juegos(ctx):
    await ctx.send(f'Aqui estan los juegos que puedes Jugar, Poki, Roblox, Haxball, Juegos Friv, Minijuegos, Ajedrez, Gartic_phone, Cookie_Clicker y Akinator, Escribe el nombre del juego que quieras jugar, si ninguno de los juegos te interasan pon $Steam para descargar juegos que te puedan interesar.')


@bot.command()
async def Haxball(ctx):
    await ctx.send(f'https://www.haxball.com/play  Aqui esta el enlace para jugarlo, Informacion: HaxBall es un juego multijugador en tiempo real que mezcla el fútbol y el hockey sobre aire.Los jugadores pueden crear o entrar en salas para competir contra otros usuarios, ya sea por equipos o individualmente.')

@bot.command()
async def Poki(ctx):
    await ctx.send(f' https://poki.com/es#utm_source=redirect-en-es  Aqui esta el enlace para jugarlo, Informacion: Poki es una página en línea que permite que sus usuarios jueguen cientos de títulos sin necesidad de descargarlos.')
   
@bot.command()
async def Roblox(ctx):
    await ctx.send(f'  https://www.roblox.com/es  Aqui esta el enlace para jugarlo y que te registres, Informacion: Roblox es una plataforma de videojuegos multijugador y de creación de videojuegos en línea. Los usuarios pueden crear y compartir sus propios mundos virtuales, llamados experiencias.   ¿Como registrarte en roblox?  1- Pon tu fecha de nacimiento, Dia, Mes y Año.     2- Pon el nombre que te quieras poner, con la condicion de que ese nombre no este en uso.      3- Pon una contraseña con minimo 8 caracteres, te recomiendo que sea una contraseña que no tenga criterios personales.     4- Pon tu genero: Masculino o femenino (opcional)')

@bot.command()
async def Juegos_Friv(ctx):
    await ctx.send(f'https://www.friv.com/?play-juegos Aqui esta el enlace para jugarlo, Informacion: Informacion: Juegos Friv es una página en línea que permite que sus usuarios jueguen cientos de títulos sin necesidad de descargarlos.')

@bot.command()
async def Minijuegos(ctx):
    await ctx.send(f'https://www.minijuegos.com/ Aqui esta el enlace para jugarlo, Informacion: Minijuegos es una página en línea que permite que sus usuarios jueguen cientos de títulos sin necesidad de descargarlos.')

@bot.command()
async def Ajedrez(ctx):
    await ctx.send(f'https://www.chess.com/es Aqui esta el enlace para jugarlo, Informacion: El ajedrez es un juego de estrategia y habilidad que se juega en un tablero cuadriculado de 64 casillas dispuestas en un patrón de 8x8. Es uno de los juegos de mesa más antiguos y populares del mundo, con una historia que se remonta a más de mil años. ')

@bot.command()
async def Steam(ctx):
    await ctx.send(f'Aqui esta el enlace para descargar juegos por Steam https://store.steampowered.com/?l=spanish')

@bot.command()
async def Gartic_phone(ctx):
    await ctx.send(f'Aqui esta el enlace para jugarlo https://garticphone.com/es Informacion: Gartic Phone es un juego en línea que combina la creatividad con la comunicación. Se juega en un navegador web y permite a los participantes dibujar y adivinar, en una especie de teléfono descompuesto digital. Cada participante debe escribir una frase, que luego será dibujada por otro jugador')

@bot.command()
async def Cookie_Clicker(ctx):
    await ctx.send(f'Aqui esta el enlace para jugarlo https://cookieclicker.com/ Informacion: El objetivo del juego es producir tantas galletas como puedas, haciendo clic en una galleta grande en la pantalla y obteniendo una sola galleta por clic.')

@bot.command()
async def Akinator(ctx):
    await ctx.send(f'Aqui esta el enlace para jugarlo https://es.akinator.com/ Informacion: Akinator es un programa de inteligencia artificial que adivina personajes reales o ficticios en los que estás pensando')







@bot.command()
async def hacker(ctx, count_hacks = 5):
    await ctx.send("hacks" * count_hacks)

@bot.command()
async def adios(ctx):
    await ctx.send('¡Hasta luego! Que tengas un buen día.')

@bot.command()
async def noticia(ctx):
    await ctx.send('Última noticia: ¡Hoy es un gran día para aprender nuevos juegos con tu bot de Discord!')

@bot.command()
async def emoji(ctx):
    await ctx.send(f'👍')

@bot.command()
async def image(ctx):
    with open('imagen/Gatos.jpeg', 'rb') as f:
        picture = discord.File(f)
    await ctx.send (file = picture)   

@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_url = attachment.url
            await attachment.save(f"./{attachment.filename}")
            await ctx.send(f"se ha guardado ./{attachment.filename}")
    else:
        await ctx.send("Olvidaste subir la imagen :(")

bot.run("Aqui va el TOKEN")