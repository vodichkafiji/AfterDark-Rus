





define ad_discord_rpc_application_id = "1543672830837784668"






default persistent.ad_discord_rpc_enabled = True





init -999 python:
    import os
    import sys

    ad_discord_rpc_package_path = os.path.join(
    renpy.config.gamedir,
    "oscar assets",
    "python-packages"
)

    if ad_discord_rpc_package_path not in sys.path:
        sys.path.insert(0, ad_discord_rpc_package_path)


init -900 python:


    import time as ad_discord_rpc_time

    try:
        import pypresence
        from pypresence.exceptions import DiscordError, DiscordNotFound
    except Exception:
        pypresence = None
        DiscordError = Exception
        DiscordNotFound = Exception





    import threading as ad_rpc_threading

    def ad_discord_rpc_worker(runtime, presence_class):
        presence = None
        active_id = None
        last_payload = None
        next_update = 0.0
        try:
            while not runtime["stop"].is_set():
                runtime["wake"].wait(1.0)
                runtime["wake"].clear()
                if runtime["stop"].is_set():
                    break
                with runtime["lock"]:
                    enabled, application_id, version = runtime["desired"]
                if presence is not None and (not enabled or application_id != active_id):
                    try:
                        presence.close()
                    except Exception:
                        pass
                    presence = None
                    last_payload = None
                    next_update = 0.0
                if not enabled or not application_id:
                    continue
                now = ad_discord_rpc_time.monotonic()
                if now < next_update:
                    continue
                try:
                    if presence is None:
                        presence = presence_class(application_id, connection_timeout=2, response_timeout=2)
                        presence.connect()
                        active_id = application_id
                    payload = (application_id, version)
                    if payload != last_payload:
                        presence.update(details="v{}".format(version))
                        last_payload = payload
                    next_update = now + 30.0
                except Exception:
                    if presence is not None:
                        try:
                            presence.close()
                        except Exception:
                            pass
                    presence = None
                    last_payload = None
                    next_update = now + 15.0
        finally:
            if presence is not None:
                try:
                    presence.close()
                except Exception:
                    pass

    def ad_discord_rpc_runtime():
        runtime = getattr(renpy, "_ad_discord_rpc_runtime", None)
        if runtime is None or "worker" not in runtime or not runtime["worker"].is_alive():
            if pypresence is None:
                return None
            runtime = {
            "desired": (False, "", ""),
            "lock": ad_rpc_threading.Lock(),
            "wake": ad_rpc_threading.Event(),
            "stop": ad_rpc_threading.Event(),
        }
            runtime["worker"] = ad_rpc_threading.Thread(
            target=ad_discord_rpc_worker, args=(runtime, pypresence.Presence),
            name="oscar-discord-rpc", daemon=True)
            setattr(renpy, "_ad_discord_rpc_runtime", runtime)
            runtime["worker"].start()
        return runtime

    def ad_discord_rpc_refresh(force=False):
        runtime = ad_discord_rpc_runtime()
        if runtime is None:
            return False
        desired = (
        bool(getattr(renpy.store.persistent, "ad_discord_rpc_enabled", True)),
        str(getattr(renpy.store, "ad_discord_rpc_application_id", "")),
        str(renpy.config.version),
    )
        with runtime["lock"]:
            changed = desired != runtime["desired"]
            runtime["desired"] = desired
        if changed or force:
            runtime["wake"].set()
        return True

    def ad_discord_rpc_start():
        ad_discord_rpc_refresh(force=True)

    def ad_discord_rpc_on_interact():
        ad_discord_rpc_refresh()

    def ad_discord_rpc_close():
        runtime = getattr(renpy, "_ad_discord_rpc_runtime", None)
        if runtime and "stop" in runtime:
            runtime["stop"].set()
            runtime["wake"].set()

    def ad_discord_rpc_set_enabled(enabled):
        renpy.store.persistent.ad_discord_rpc_enabled = enabled
        ad_discord_rpc_refresh(force=True)
        renpy.restart_interaction()

    config.start_callbacks.append(ad_discord_rpc_start)
    config.interact_callbacks.append(ad_discord_rpc_on_interact)
    config.after_load_callbacks.append(ad_discord_rpc_start)
    config.quit_callbacks.append(ad_discord_rpc_close)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
