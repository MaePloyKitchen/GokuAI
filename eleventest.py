from elevenlabs import generate, play,set_api_key, save

set_api_key("YOUR KEY HERE")

audio = generate(
    text="The weather there is sunny!",
    voice="Goku",
    model='eleven_monolingual_v1'
)

save(audio,"weather_1.mp3")

play(audio)
