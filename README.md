# SpeechToTextAPI

This is an API that will accept an audio file, transcribe it, and then return the transcription.

Transcriptions are done using the speech_recognition library, making use of the google_speech API.

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

~~Will explain the endpoint later, when I figure out everything else.~~
I figured everything else out for the most part, but I'm still not good enough with javascript to explain it!
You can refer to [this application](https://github.com/IsaiahSama/SelfWhisperer) in the "Record.js" file, to see an example though.
