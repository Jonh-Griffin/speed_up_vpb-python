import json
import random

def gerar_arma(nome, tipo, max_ammo, dano, rpm):
    return {
        "name": nome,
        "type": tipo,
        "maxAmmoCapacity": max_ammo,
        "compatibleAmmo": ["ammocreative", "ammo50bmg"],
        "damage": dano,
        "rpm": rpm,
        "fireModes": ["SINGLE"],
        "fireSound": "shot3",
        "drawCooldownDuration": random.randint(600, 700),
        "aimingZoom": 0.5,
        "gunRecoilInitialAmplitude": random.uniform(1.0, 2.0),
        "shakeRecoilAmplitude": random.uniform(0.1, 0.5),
        "shakeRecoilSpeed": random.uniform(2, 4),
        "viewRecoilAmplitude": random.uniform(5, 10),
        "inspectCooldownDuration": random.randint(4000, 5000),
        "compatibleAttachments": ["cantedrail"],
        "compatibleAttachmentGroups": [
            "ar_sightsandscopes",
            "snipers_sights",
            "ammo"
        ],
        "phasedReloads": gerar_fases_recarregamento(),
        "effects": gerar_efeitos(),
        "features": gerar_recursos()
    }

def gerar_fases_recarregamento():
    return [
        {
            "phase": "RELOADING",
            "condition": "reloadIterationIndex == 0",
            "duration": random.randint(4000, 4500),
            "animation": "animation.model.reloadempty",
            "shakeEffects": gerar_efeitos_shake()
        },
        {
            "phase": "RELOADING",
            "condition": "reloadIterationIndex > 0",
            "duration": random.randint(2500, 2700),
            "animation": "animation.model.reload",
            "shakeEffects": gerar_efeitos_shake()
        }
    ]

def gerar_efeitos_shake():
    return [
        {
            "start": 0,
            "duration": random.randint(1000, 2000),
            "initialAmplitude": random.uniform(0.1, 0.3),
            "rateOfAmplitudeDecay": random.uniform(0.3, 0.8)
        },
        {
            "start": random.randint(200, 500),
            "duration": random.randint(500, 1500),
            "initialAmplitude": random.uniform(0.1, 0.3),
            "rateOfAmplitudeDecay": random.uniform(0.3, 0.8)
        }
    ]

def gerar_efeitos():
    return [
        {
            "phase": "hit_scan_acquired",
            "name": "tracer"
        },
        {
            "phase": "firing",
            "name": "muzzle_flash"
        }
    ]

def gerar_recursos():
    return [
        {
            "type": "Aiming",
            "zoom": 0.5,
            "condition": {
                "doesNotHaveAttachmentGroup": "ar_sightsandscopes"
            }
        },
        {
            "type": "MuzzleFlash",
            "effects": [
                {
                    "phase": "firing",
                    "name": "muzzle_flash"
                }
            ],
            "condition": {
                "allOf": [
                    {
                        "isUsingDefaultMuzzle": True
                    },
                    {
                        "doesNotHaveAttachment": "hp_suppressor"
                    }
                ]
            }
        }
    ]


# Gera a arma
arma = gerar_arma("m82a1", "Gun", 10, 40.0, 115)

# Converte para JSON sem ser em linha unica
arma_json = json.dumps(arma, indent=2)

# Salva em um arquivo
with open('arma.json', 'w') as f:
    f.write(arma_json)

print("Arma gerada e salva em 'arma.json'")

pronpt = True
while pronpt:
    input("command: ")


    if input("command: ") == "exit":
        pronpt = False

#Para por aqui, preguiça da p****