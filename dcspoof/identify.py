MODES = {
    "vr": {
        "$os": "android",
        "$browser": "Discord VR",
        "$device": "oculus",
    },
    "ios": {
        "$os": "Discord iOS",
        "$browser": "Discord iOS",
        "$device": "iPhone",
    },
    "android": {
        "$os": "Discord Android",
        "$browser": "Discord Android",
        "$device": "Android",
    },
    #"console": {
    #    "$os": "Windows",
    #    "$browser": "Discord",
    #    "$device": "PlayStation 5",
    #},
    "desktop": {
        "$os": "Windows",
        "$browser": "Discord Client",
        "$device": "desktop",
    },
    "web": {
        "$os": "Windows",
        "$browser": "Chrome",
        "$device": "",
    },
}


def make_identify(mode_name: str = "ios"):
    
    props = MODES.get(mode_name, MODES["ios"])

    async def identify(self):
        payload = {
            "op": self.IDENTIFY,
            "d": {
                "token": self.token,
                "properties": {
                    "$os": props["$os"],
                    "$browser": props["$browser"],
                    "$device": props["$device"],
                    "$referrer": "",
                    "$referring_domain": "",
                },
                "compress": True,
                "large_threshold": 250,
            },
        }

        if self.shard_id is not None and self.shard_count is not None:
            payload["d"]["shard"] = [self.shard_id, self.shard_count]

        state = self._connection
        if state._activity is not None or state._status is not None:
            payload["d"]["presence"] = {
                "status": state._status,
                "game": state._activity,
                "since": 0,
                "afk": False,
            }

        if state._intents is not None:
            payload["d"]["intents"] = state._intents.value

        await self.call_hooks("before_identify", self.shard_id, initial=self._initial_identify)
        await self.send_as_json(payload)

    return identify
