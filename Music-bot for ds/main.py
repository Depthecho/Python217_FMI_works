import discord
from discord.ext import commands
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Установка данных клиента Spotify
client_id = '377f823aab8a4d8aa57118fbdceeb1aa'
client_secret = '6fc926b435ad412198e8995055ad002b'
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id, client_secret))

# Установка токена бота Discord
discord_token = 'MTExODQwODYzMDQ4ODgwNTQ4MA.GnoeUy.SecNVJM1sOBB7__hwYzn6dR4lhxjRiLp9TQnlk'

# Создание объекта клиента Discord
intents = discord.Intents.default()
intents.voice_states = True
bot = commands.Bot(command_prefix='+', intents=intents)


# Функция для поиска трека в Spotify
def search_track(query):
    results = spotify.search(q=query, type='track')
    if results['tracks']['items']:
        track_uri = results['tracks']['items'][0]['uri']
        return track_uri
    else:
        return None


# Функция для воспроизведения трека
async def play_track(ctx, track_uri):
    voice_channel = ctx.author.voice.channel
    if not voice_channel:
        await ctx.send("Вы должны находиться в голосовом канале, чтобы воспроизвести музыку.")
        return

    voice_client = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if voice_client and voice_client.channel != voice_channel:
        await voice_client.move_to(voice_channel)
    elif not voice_client:
        voice_client = await voice_channel.connect()

    voice_client.stop()
    voice_client.play(discord.FFmpegPCMAudio(track_uri))


# Команда для воспроизведения трека из Spotify по названию или ссылке
@bot.command()
async def p(ctx, *, query):
    track_uri = search_track(query)
    if track_uri:
        await play_track(ctx, track_uri)
    else:
        await ctx.send("Не удалось найти трек в Spotify.")


# Команда для приостановки воспроизведения
@bot.command()
async def n(ctx):
    voice_client = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if voice_client and voice_client.is_playing():
        voice_client.pause()


# Команда для возобновления воспроизведения
@bot.command()
async def s(ctx):
    voice_client = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if voice_client and voice_client.is_paused():
        voice_client.resume()


# Команда для пропуска текущего трека
@bot.command()
async def skip(ctx):
    voice_client = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if voice_client and voice_client.is_playing():
        voice_client.stop()


# Команда для отключения от голосового канала
@bot.command()
async def d(ctx):
    voice_client = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if voice_client:
        await voice_client.disconnect()


# Обработчик события готовности бота
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')


# Запуск бота
bot.run(discord_token)
