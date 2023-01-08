from federatedsecure.server.builtins.util.kvstorage import KeyValueStorage


def federatedsecure_register(registry):

    registry.register(
        {
            "namespace": "federatedsecure",
            "plugin": "Util",
            "version": "0.5.3",
            "microservice": "KeyValueStorage"
        },
        KeyValueStorage()
    )
