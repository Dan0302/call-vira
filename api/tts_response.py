import boto3
import os

def synthesize_speech(text: str, voice_id: str = "Vicki", output_path: str = "response.mp3") -> str:
    polly = boto3.client(
        "polly",
        region_name="eu-central-1",
        aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
        aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY")
    )

    response = polly.synthesize_speech(
        Text=text,
        OutputFormat="mp3",
        VoiceId=voice_id,
        LanguageCode="de-DE"
    )

    if "AudioStream" in response:
        with open(output_path, "wb") as f:
            f.write(response["AudioStream"].read())
        return output_path
    else:
        raise Exception("Text-to-Speech fehlgeschlagen.")