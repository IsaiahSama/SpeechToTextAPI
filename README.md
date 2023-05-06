# SpeechToTextAPI

This is an API that will accept an audio file, transcribe it, and then return the transcription.

Not sure what I'm going to use to transcribe as yet, but it'll be cool.

## Endpoints

/transcribe/ - POST

### /transcribe/

This endpoint is a POST only. This endpoint expects JSON to be sent in the following format:

```js
{
    method: "POST",
    body: formData,
    headers: {
        "Content-Type": "multipart/form-data",
    },
}
```

Where formData contains the audio file to be transcribed under the key 'audio'.

For Example:

```js
const formData = new FormData();
formData.append("audio", file);
```

Will explain the endpoint later, when I figure out everything else.
