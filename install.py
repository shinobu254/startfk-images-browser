import neko

if not neko.is_installed("send2trash"):
    neko.run_pip("install Send2Trash", "Send2Trash requirement for image browser")
