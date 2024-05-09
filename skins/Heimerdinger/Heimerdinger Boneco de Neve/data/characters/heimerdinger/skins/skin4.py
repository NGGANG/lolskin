#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {
    "DATA/Heimerdinger_Skins_Skin0_Skins_Skin1_Skins_Skin2_Skins_Skin3_Skins_Skin4_Skins_Skin5.bin"
    "DATA/Heimerdinger_Skins_Skin0_Skins_Skin1_Skins_Skin15_Skins_Skin16_Skins_Skin17_Skins_Skin18_Skins_Skin19_Skins_Skin2_Skins_Skin20_Skins_Skin21_Skins_Skin22_Skins_Skin23_Skins_Skin24_Skins_Skin25_Skins_Skin26_Skins_Skin27_Skins_Skin28_Skins_Skin29_Skins_Skin3_Skins_Skin30_Skins_Skin31_Skins_Skin32_Skins_Skin4_Skins_Skin5.bin"
    "DATA/Characters/Heimerdinger/Heimerdinger.bin"
    "DATA/Heimerdinger_Skins_Skin0_Skins_Skin1_Skins_Skin2_Skins_Skin3_Skins_Skin4.bin"
    "DATA/Characters/Heimerdinger/Animations/Skin0.bin"
    "DATA/Heimerdinger_Skins_Root_Skins_Skin0_Skins_Skin1_Skins_Skin2_Skins_Skin3_Skins_Skin4.bin"
    "DATA/Heimerdinger_Skins_Skin0_Skins_Skin1_Skins_Skin2_Skins_Skin24_Skins_Skin25_Skins_Skin26_Skins_Skin27_Skins_Skin28_Skins_Skin29_Skins_Skin3_Skins_Skin30_Skins_Skin31_Skins_Skin32_Skins_Skin4_Skins_Skin5.bin"
}
entries: map[hash,embed] = {
   "Characters/Heimerdinger/Skins/Skin0" = SkinCharacterDataProperties {
        SkinClassification: u32 = 1
        ChampionSkinName: string = "HeimerdingerSkin04"
        MetaDataTags: string = "faction:piltover,gender:male,race:yordle,element:ice,skinline:snowdown"
        Loadscreen: embed = CensoredImage {
            Image: string = "ASSETS/Characters/Heimerdinger/Skins/Skin04/HeimerdingerLoadScreen_4.dds"
        }
        SkinAudioProperties: embed = SkinAudioProperties {
            TagEventList: list[string] = {
                "Heimerdinger"
            }
            BankUnits: list2[embed] = {
                BankUnit {
                    Name: string = "Heimerdinger_Base_SFX"
                    BankPath: list[string] = {
                        "ASSETS/Sounds/Wwise2016/SFX/Characters/Heimerdinger/Skins/Base/Heimerdinger_Base_SFX_audio.bnk"
                        "ASSETS/Sounds/Wwise2016/SFX/Characters/Heimerdinger/Skins/Base/Heimerdinger_Base_SFX_events.bnk"
                    }
                    Events: list[string] = {
                        "Play_sfx_Heimerdinger_Dance3D_buffactivate"
                        "Play_sfx_Heimerdinger_Dance3D_cast"
                        "Play_sfx_Heimerdinger_Death3D_cast"
                        "Play_sfx_Heimerdinger_HeimerdingerBasicAttack2_OnCast"
                        "Play_sfx_Heimerdinger_HeimerdingerBasicAttack2_OnHit"
                        "Play_sfx_Heimerdinger_HeimerdingerBasicAttack2_OnMissileLaunch"
                        "Play_sfx_Heimerdinger_HeimerdingerBasicAttack_OnCast"
                        "Play_sfx_Heimerdinger_HeimerdingerBasicAttack_OnHit"
                        "Play_sfx_Heimerdinger_HeimerdingerBasicAttack_OnMissileLaunch"
                        "Play_sfx_Heimerdinger_HeimerdingerCritAttack_OnCast"
                        "Play_sfx_Heimerdinger_HeimerdingerCritAttack_OnHit"
                        "Play_sfx_Heimerdinger_HeimerdingerCritAttack_OnMissileLaunch"
                        "Play_sfx_Heimerdinger_HeimerdingerE_OnCast"
                        "Play_sfx_Heimerdinger_HeimerdingerESpell_hit"
                        "Play_sfx_Heimerdinger_HeimerdingerESpell_OnMissileLaunch"
                        "Play_sfx_Heimerdinger_HeimerdingerESpell_Ult_hit"
                        "Play_sfx_Heimerdinger_HeimerdingerESpell_Ult_OnMissileLaunch"
                        "Play_sfx_Heimerdinger_HeimerdingerEUlt_OnCast"
                        "Play_sfx_Heimerdinger_HeimerdingerQ_OnCast"
                        "Play_sfx_Heimerdinger_HeimerdingerR_OnBuffActivate"
                        "Play_sfx_Heimerdinger_HeimerdingerR_OnBuffDeactivate"
                        "Play_sfx_Heimerdinger_HeimerdingerSuperTurret_OnBuffActivate"
                        "Play_sfx_Heimerdinger_HeimerdingerSuperTurret_OnBuffDeactivate"
                        "Play_sfx_Heimerdinger_HeimerdingerW_OnCast"
                        "Play_sfx_Heimerdinger_HeimerdingerWAttack2_hit"
                        "Play_sfx_Heimerdinger_HeimerdingerWAttack2_OnMissileCast"
                        "Play_sfx_Heimerdinger_HeimerdingerWAttack2_OnMissileLaunch"
                        "Play_sfx_Heimerdinger_HeimerdingerWAttack2Ult_hit"
                        "Play_sfx_Heimerdinger_HeimerdingerWAttack2Ult_OnMissileLaunch"
                        "Play_sfx_Heimerdinger_Idle2_buffactivate"
                        "Play_sfx_Heimerdinger_Recall3D_buffactivate"
                        "Play_sfx_Heimerdinger_Respawn3D_buffactivate"
                        "Play_sfx_Heimerdinger_Taunt3D_buffactivate"
                        "Play_sfx_HeimerTBlue_HeimerdingerRQEngineAudio_OnBuffActivate"
                        "Play_sfx_HeimerTBlue_HeimerdingerTurretBigEnergyBlast_OnCast"
                        "Play_sfx_HeimerTBlue_HeimerdingerTurretBigEnergyBlast_OnHit"
                        "Play_sfx_HeimerTBlue_HeimerdingerTurretBigEnergyBlast_OnMissileLaunch"
                        "Play_sfx_HeimerTBlue_HeimerTBlueBasicAttack_OnCast"
                        "Play_sfx_HeimerTBlue_HeimerTBlueBasicAttack_OnHit"
                        "Play_sfx_HeimerTBlue_HeimerTBlueBasicAttack_OnMissileLaunch"
                        "Play_sfx_HeimerTYellow_HeimerdingerEngineAudio_OnBuffActivate"
                        "Play_sfx_HeimerTYellow_HeimerdingerEngineAudio_turrettalk_buffactivate"
                        "Play_sfx_HeimerTYellow_HeimerdingerQSpawnDestroyAudio_OnBuffActivate"
                        "Play_sfx_HeimerTYellow_HeimerdingerQSpawnDestroyAudio_OnBuffDeactivate"
                        "Play_sfx_HeimerTYellow_HeimerdingerTurretEnergyBlast_OnCast"
                        "Play_sfx_HeimerTYellow_HeimerdingerTurretEnergyBlast_OnHit"
                        "Play_sfx_HeimerTYellow_HeimerdingerTurretEnergyBlast_OnMissileLaunch"
                        "Play_sfx_HeimerTYellow_HeimerTurretShutdown_OnBuffActivate"
                        "Play_sfx_HeimerTYellow_HeimerTurretShutdown_OnBuffDeactivate"
                        "Play_sfx_HeimerTYellow_HeimerTYellowBasicAttack2_OnCast"
                        "Play_sfx_HeimerTYellow_HeimerTYellowBasicAttack2_OnHit"
                        "Play_sfx_HeimerTYellow_HeimerTYellowBasicAttack2_OnMissileLaunch"
                        "Play_sfx_HeimerTYellow_HeimerTYellowBasicAttack_OnCast"
                        "Play_sfx_HeimerTYellow_HeimerTYellowBasicAttack_OnHit"
                        "Play_sfx_HeimerTYellow_HeimerTYellowBasicAttack_OnMissileLaunch"
                        "Stop_sfx_Heimerdinger_HeimerdingerBasicAttack2_OnMissileLaunch"
                        "Stop_sfx_Heimerdinger_HeimerdingerBasicAttack_OnMissileLaunch"
                        "Stop_sfx_Heimerdinger_HeimerdingerCritAttack_OnMissileLaunch"
                        "Stop_sfx_Heimerdinger_HeimerdingerESpell_OnMissileLaunch"
                        "Stop_sfx_Heimerdinger_HeimerdingerESpell_Ult_OnMissileLaunch"
                        "Stop_sfx_Heimerdinger_HeimerdingerWAttack2_OnMissileLaunch"
                        "Stop_sfx_Heimerdinger_HeimerdingerWAttack2Ult_OnMissileLaunch"
                        "Stop_sfx_HeimerTBlue_HeimerdingerRQEngineAudio_OnBuffActivate"
                        "Stop_sfx_HeimerTBlue_HeimerdingerTurretBigEnergyBlast_OnMissileLaunch"
                        "Stop_sfx_HeimerTYellow_HeimerdingerEngineAudio_OnBuffActivate"
                        "Stop_sfx_HeimerTYellow_HeimerdingerTurretEnergyBlast_OnMissileLaunch"
                        "Stop_sfx_HeimerYellow_HeimerdingerQSpawnDestroyAudio_OnBuffActivate"
                    }
                }
                BankUnit {
                    Name: string = "Heimerdinger_Base_VO"
                    BankPath: list[string] = {
                        "ASSETS/Sounds/Wwise2016/VO/en_US/Characters/Heimerdinger/Skins/Base/Heimerdinger_Base_VO_audio.bnk"
                        "ASSETS/Sounds/Wwise2016/VO/en_US/Characters/Heimerdinger/Skins/Base/Heimerdinger_Base_VO_events.bnk"
                        "ASSETS/Sounds/Wwise2016/VO/en_US/Characters/Heimerdinger/Skins/Base/Heimerdinger_Base_VO_audio.wpk"
                    }
                    Events: list[string] = {
                        "Play_vo_Heimerdinger_Attack2DGeneral"
                        "Play_vo_Heimerdinger_Death3D"
                        "Play_vo_Heimerdinger_FirstEncounter3DJayce"
                        "Play_vo_Heimerdinger_FirstEncounter3DVelkoz"
                        "Play_vo_Heimerdinger_FirstEncounter3DVi"
                        "Play_vo_Heimerdinger_FirstEncounter3DViktor"
                        "Play_vo_Heimerdinger_FirstEncounter3DZiggs"
                        "Play_vo_Heimerdinger_HeimerdingerBasicAttack2_cast3D"
                        "Play_vo_Heimerdinger_HeimerdingerBasicAttack_cast3D"
                        "Play_vo_Heimerdinger_HeimerdingerCritAttack_cast3D"
                        "Play_vo_Heimerdinger_HeimerdingerE_cast3D"
                        "Play_vo_Heimerdinger_HeimerdingerEUlt_cast3D"
                        "Play_vo_Heimerdinger_HeimerdingerQ_cast3D"
                        "Play_vo_Heimerdinger_HeimerdingerQUlt_cast3D"
                        "Play_vo_Heimerdinger_HeimerdingerR_cast3D"
                        "Play_vo_Heimerdinger_HeimerdingerW_cast3D"
                        "Play_vo_Heimerdinger_HeimerdingerWUlt_cast3D"
                        "Play_vo_Heimerdinger_Joke3DGeneral"
                        "Play_vo_Heimerdinger_Laugh3DGeneral"
                        "Play_vo_Heimerdinger_Move2DStandard"
                        "Play_vo_Heimerdinger_Recall3DGeneral"
                        "Play_vo_Heimerdinger_Taunt3DGeneral"
                    }
                    VoiceOver: bool = true
                }
            }
        }
        SkinAnimationProperties: embed = SkinAnimationProperties {
            AnimationGraphData: link = "Characters/Heimerdinger/Animations/Skin0"
        }
        SkinMeshProperties: embed = SkinMeshDataProperties {
            Skeleton: string = "ASSETS/Characters/Heimerdinger/Skins/Skin04/Heimerdinger_Snowman.skl"
            SimpleSkin: string = "ASSETS/Characters/Heimerdinger/Skins/Skin04/Heimerdinger_Snowman.skn"
            Texture: string = "ASSETS/Characters/Heimerdinger/Skins/Skin04/heimerdinger_snowman_TX_CM.dds"
            SkinScale: f32 = 0.899999976
            SelfIllumination: f32 = 0.699999988
            OverrideBoundingBox: option[vec3] = {
                { 100, 200, 100 }
            }
            ReflectionFresnelColor: rgba = { 0, 0, 0, 255 }
            InitialSubmeshToHide: string = "Heimerdinger_Grab_Hand, Heimerdinger_Antenna"
        }
        ArmorMaterial: string = "Flesh"
        DefaultAnimations: list[string] = {
            "North_Adjust"
            "Iris_default"
        }
        ExtraCharacterPreloads: list[string] = {
            "HeimerTYellow"
            "HeimerTBlue"
        }
        IconAvatar: string = "ASSETS/Characters/Heimerdinger/HUD/Heimerdinger_Circle_4.dds"
        mContextualActionData: link = "Characters/Heimerdinger/CAC/Heimerdinger_Base"
        IconCircle: option[string] = {
            "ASSETS/Characters/Heimerdinger/HUD/Heimerdinger_Circle.dds"
        }
        IconSquare: option[string] = {
            "ASSETS/Characters/Heimerdinger/HUD/Heimerdinger_Square.dds"
        }
        HealthBarData: embed = CharacterHealthBarDataRecord {
            UnitHealthBarStyle: u8 = 10
        }
        mEmblems: list[embed] = {
            SkinEmblem {
                mEmblemData: link = "Emblems/9"
            }
        }
        mResourceResolver: link = "Characters/Heimerdinger/Skins/Skin4/Resources"
    }
    "Characters/Heimerdinger/Skins/Skin0/Resources" = ResourceResolver {
        ResourceMap: map[hash,link] = {
            0xc38446b9 = "Characters/Heimerdinger/Skins/Skin0/Particles/HeimerdingerScrapRelic"
            "Heimerdinger_AA_2_mis" = "Characters/Heimerdinger/Skins/Skin4/Particles/Heimerdinger_Skin04_AA_2_mis"
            "Heimerdinger_AA_mis" = "Characters/Heimerdinger/Skins/Skin4/Particles/Heimerdinger_Skin04_AA_mis"
            "Heimerdinger_AA_Tar" = "Characters/Heimerdinger/Skins/Skin0/Particles/Heimerdinger_Base_AA_Tar"
            "Heimerdinger_Crit_mis" = "Characters/Heimerdinger/Skins/Skin4/Particles/Heimerdinger_Skin04_Crit_mis"
            "Heimerdinger_Crit_Tar" = "Characters/Heimerdinger/Skins/Skin0/Particles/Heimerdinger_Base_Crit_Tar"
            "Heimerdinger_Dance_Rocket" = "Characters/Heimerdinger/Skins/Skin0/Particles/Heimerdinger_Base_Dance_Rocket"
            "Heimerdinger_Dance_Rocket_Start" = "Characters/Heimerdinger/Skins/Skin0/Particles/Heimerdinger_Base_Dance_Rocket_Start"
            "Heimerdinger_Death_Explosion_01" = "Characters/Heimerdinger/Skins/Skin0/Particles/Heimerdinger_Base_Death_Explosion_01"
            "Heimerdinger_E_Cas" = "Characters/Heimerdinger/Skins/Skin0/Particles/Heimerdinger_Base_E_Cas"
            "Heimerdinger_E_Cas_Ult" = "Characters/Heimerdinger/Skins/Skin0/Particles/Heimerdinger_Base_E_Cas_Ult"
            "Heimerdinger_E_Explosion" = "Characters/Heimerdinger/Skins/Skin0/Particles/Heimerdinger_Base_E_Explosion"
            "Heimerdinger_E_Explosion_Ult" = "Characters/Heimerdinger/Skins/Skin0/Particles/Heimerdinger_Base_E_Explosion_Ult"
            "Heimerdinger_E_Explosion_Ult_End" = "Characters/Heimerdinger/Skins/Skin0/Particles/Heimerdinger_Base_E_Explosion_Ult_End"
            "Heimerdinger_E_Mis" = "Characters/Heimerdinger/Skins/Skin0/Particles/Heimerdinger_Base_E_Mis"
            "Heimerdinger_E_Mis_Ult" = "Characters/Heimerdinger/Skins/Skin0/Particles/Heimerdinger_Base_E_Mis_Ult"
            "Heimerdinger_E_Tar" = "Characters/Heimerdinger/Skins/Skin0/Particles/Heimerdinger_Base_E_Tar"
            "Heimerdinger_E_Ult_Cas" = "Characters/Heimerdinger/Skins/Skin0/Particles/Heimerdinger_Base_E_Ult_Cas"
            "Heimerdinger_Homeguard_Rocket" = "Characters/Heimerdinger/Skins/Skin0/Particles/Heimerdinger_Base_Homeguard_Rocket"
            "Heimerdinger_Homeguard_Rocket_In" = "Characters/Heimerdinger/Skins/Skin0/Particles/Heimerdinger_Base_Homeguard_Rocket_In"
            "Heimerdinger_Q_aggro" = "Characters/Heimerdinger/Skins/Skin0/Particles/Heimerdinger_Base_Q_aggro"
            "Heimerdinger_Q_Ammo_Spend" = "Characters/Heimerdinger/Skins/Skin0/Particles/Heimerdinger_Base_Q_Ammo_Spend"
            "Heimerdinger_Q_Cas" = "Characters/Heimerdinger/Skins/Skin0/Particles/Heimerdinger_Base_Q_Cas"
            "Heimerdinger_Q_Cas_Ult" = "Characters/Heimerdinger/Skins/Skin0/Particles/Heimerdinger_Base_Q_Cas_Ult"
            "Heimerdinger_Q_directAggro" = "Characters/Heimerdinger/Skins/Skin0/Particles/Heimerdinger_Base_Q_directAggro"
            "Heimerdinger_Q_target" = "Characters/Heimerdinger/Skins/Skin0/Particles/Heimerdinger_Base_Q_target"
            "Heimerdinger_Q_Turret_Charge_Up" = "Characters/Heimerdinger/Skins/Skin0/Particles/Heimerdinger_Base_Q_Turret_Charge_Up"
            "Heimerdinger_Q_Turret_Exclamation" = "Characters/Heimerdinger/Skins/Skin0/Particles/Heimerdinger_Base_Q_Turret_Exclamation"
            0xb92b4e10 = "Characters/Heimerdinger/Skins/Skin0/Particles/heimerdinger_base_recall_sound"
            "Heimerdinger_Recall_Start" = "Characters/Heimerdinger/Skins/Skin0/Particles/Heimerdinger_Base_Recall_Start"
            "Heimerdinger_R_Antenna_Glow" = "Characters/Heimerdinger/Skins/Skin0/Particles/Heimerdinger_Base_R_Antenna_Glow"
            "Heimerdinger_R_Beam" = "Characters/Heimerdinger/Skins/Skin0/Particles/Heimerdinger_Base_R_Beam"
            "Heimerdinger_R_Cast" = "Characters/Heimerdinger/Skins/Skin0/Particles/Heimerdinger_Base_R_Cast"
            "Heimerdinger_R_MegaTurret_Charge_Up" = "Characters/Heimerdinger/Skins/Skin0/Particles/Heimerdinger_Base_R_MegaTurret_Charge_Up"
            "Heimerdinger_R_MegaTurret_Spawn" = "Characters/Heimerdinger/Skins/Skin0/Particles/Heimerdinger_Base_R_MegaTurret_Spawn"
            "Heimerdinger_W_Cas" = "Characters/Heimerdinger/Skins/Skin0/Particles/Heimerdinger_Base_W_Cas"
            "Heimerdinger_W_Cas_Ult" = "Characters/Heimerdinger/Skins/Skin0/Particles/Heimerdinger_Base_W_Cas_Ult"
            "Heimerdinger_W_Mis_Child" = "Characters/Heimerdinger/Skins/Skin0/Particles/Heimerdinger_Base_W_Mis_Child"
            "Heimerdinger_W_Mis" = "Characters/Heimerdinger/Skins/Skin0/Particles/Heimerdinger_Base_W_Mis"
            "Heimerdinger_W_Mis_Ult_Child" = "Characters/Heimerdinger/Skins/Skin0/Particles/Heimerdinger_Base_W_Mis_Ult_Child"
            "Heimerdinger_W_Mis_Ult" = "Characters/Heimerdinger/Skins/Skin0/Particles/Heimerdinger_Base_W_Mis_Ult"
            "Heimerdinger_W_Tar" = "Characters/Heimerdinger/Skins/Skin0/Particles/Heimerdinger_Base_W_Tar"
            "Heimerdinger_W_ULT_Tar" = "Characters/Heimerdinger/Skins/Skin0/Particles/Heimerdinger_Base_W_ULT_Tar"
            0x8df85c7c = "Characters/Heimerdinger/Skins/Skin0/Particles/heimerdinger_basicAttack_mis"
            0x199f85b0 = "Characters/Heimerdinger/Skins/Skin0/Particles/heimerdinger_basicAttack_tar"
            0xfe026c5b = "Characters/Heimerdinger/Skins/Skin0/Particles/heimerdinger_emote_dance_loop_sound"
            0x9d8cc6a2 = "Characters/Heimerdinger/Skins/Skin0/Particles/heimerdinger_emote_dance_windup_sound"
            0x5665505f = "Characters/Heimerdinger/Skins/Skin0/Particles/Heimerdinger_emote_death_sound"
            0x6c8cc5c9 = "Characters/Heimerdinger/Skins/Skin0/Particles/Heimerdinger_emote_taunt_sound"
            0xea8f7d20 = "Characters/Heimerdinger/Skins/Skin0/Particles/Heimerdinger_emote_VO_longjoke"
            0xee7afd94 = "Characters/Heimerdinger/Skins/Skin0/Particles/Heimerdinger_emote_VO_shortjoke"
            0x76aa9858 = "Characters/Heimerdinger/Skins/Skin0/Particles/Heimerdinger_emote_VO_tauntbase"
            0x787748c5 = "Characters/Heimerdinger/Skins/Skin0/Particles/Heimerdinger_emote_VO_tauntjayce"
            0x02dc4a00 = "Characters/Heimerdinger/Skins/Skin0/Particles/Heimerdinger_emote_VO_tauntvelkoz"
            0x5c66fe94 = "Characters/Heimerdinger/Skins/Skin0/Particles/Heimerdinger_emote_VO_tauntvi"
            0x2bf497c6 = "Characters/Heimerdinger/Skins/Skin0/Particles/Heimerdinger_emote_VO_tauntviktor"
            0x3913c105 = "Characters/Heimerdinger/Skins/Skin0/Particles/Heimerdinger_emote_VO_tauntziggs"
            0xfbced1b0 = "Characters/Heimerdinger/Skins/Skin0/Particles/Heimerdinger_Energy"
            0x4126c3c3 = "Characters/Heimerdinger/Skins/Skin0/Particles/heimerdinger_hexTech_mis"
            0xab32683f = "Characters/Heimerdinger/Skins/Skin0/Particles/heimerdinger_hexTech_mis_ult"
            0x04f7594e = "Characters/Heimerdinger/Skins/Skin0/Particles/heimerdinger_idle2_sound"
            0x2c12f641 = "Characters/Heimerdinger/Skins/Skin0/Particles/Heimerdinger_idle_respawn_sound"
            0x00008e36 = "Characters/Heimerdinger/Skins/Skin0/Particles/Heimerdinger_InverseCharge"
            0xa0cc3e10 = "Characters/Heimerdinger/Skins/Skin0/Particles/Heimerdinger_R_Cast"
            0x7030ea33 = "Characters/Heimerdinger/Skins/Skin0/Particles/heimerdinger_slowAura_self"
            0x2e72d50e = "Characters/Heimerdinger/Skins/Skin0/Particles/Heimerdinger_TracerBeam"
            0x1e2054ae = "Characters/Heimerdinger/Skins/Skin0/Particles/Heimerdinger_TracerBeam_Allied"
            0xdb43b8dc = "Characters/Heimerdinger/Skins/Skin0/Particles/heimerdinger_turret_birth"
            0x784c560f = "Characters/Heimerdinger/Skins/Skin0/Particles/heimerdinger_turret_idle"
            0x802d3240 = "Characters/Heimerdinger/Skins/Skin0/Particles/heimerdinger_turret_idle_deactivate"
            0x04b35bad = "Characters/Heimerdinger/Skins/Skin0/Particles/Heimerdinger_turret_reanimate_sound"
            0x9993731f = "Characters/Heimerdinger/Skins/Skin0/Particles/heimerdinger_turret_ring"
            0xa52590ec = "Characters/Heimerdinger/Skins/Skin0/Particles/heimerdinger_turret_standard_mis"
            0xe581bdc0 = "Characters/Heimerdinger/Skins/Skin0/Particles/heimerdinger_turret_standard_tar"
            0x343a74f7 = "Characters/Heimerdinger/Skins/Skin0/Particles/heimerdinger_ult_turret_ring"
            0x36eaa400 = "Characters/Heimerdinger/Skins/Skin0/Particles/heimerdinger_upgrade_buf"
            0x7d06cc57 = "Characters/Heimerdinger/Skins/Skin0/Particles/Heimerdinger_VO_recall"
            "Heimer_Q_Ammo1" = "Characters/Heimerdinger/Skins/Skin0/Particles/Heimer_Base_Q_Ammo1"
            0xef0e9c20 = "Characters/Heimerdinger/Skins/Skin0/Particles/Heimer_Q_Ammo1"
            0x13e2b099 = "Characters/Heimerdinger/Skins/Skin0/Particles/Heimer_Q_Ammo2"
            0x7255e51a = "Characters/Heimerdinger/Skins/Skin0/Particles/Heimer_Q_Ammo3"
            0x97ee44f0 = "Characters/Heimerdinger/Skins/Skin0/Particles/Heimer_Q_Ammo_Spend"
            0x9616f685 = "Characters/Heimerdinger/Skins/Skin0/Particles/TurretTimer"
            0xa9b8ff53 = "Characters/Heimerdinger/Skins/Skin0/Particles/TurretTimer2"
        }
    }
    "Characters/Heimerdinger/Skins/Skin4/Particles/Heimerdinger_Skin04_AA_mis" = VfxSystemDefinitionData {
        ComplexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 120
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 0.5
                }
                EmitterName: string = "trail"
                Primitive: pointer = VfxPrimitiveArbitraryQuad {}
                Color: embed = ValueColor {
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            0.100000001
                            0.300000012
                            1
                        }
                        Values: list[vec4] = {
                            { 0.550000012, 0.349999994, 0.349999994, 0.25 }
                            { 0.449999988, 0.349999994, 0.349999994, 0.0500000007 }
                            { 0.349999994, 0.349999994, 0.349999994, 0.0500000007 }
                            { 0.349999994, 0.349999994, 0.349999994, 0 }
                        }
                    }
                }
                BirthRotation0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 0, 90 }
                }
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 90, 17, 17 }
                }
                Scale0: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            1
                        }
                        Values: list[vec3] = {
                            { 1, 1, 1 }
                            { 0.100000001, 0.100000001, 0.100000001 }
                        }
                    }
                }
                Texture: string = "ASSETS/Shared/Particles/AirSpiritStreak.DDS"
                StartFrame: u16 = 1
                TexDiv: vec2 = { 2, 2 }
            }
            VfxEmitterDefinitionData {
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 5
                }
                EmitterName: string = "candycane"
                Importance: u8 = 2
                BindWeight: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                Primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Heimerdinger/Skins/Skin04/Particles/heimerdinger_skin04_aa_candycane.scb"
                    }
                }
                BlendMode: u8 = 1
                BirthRotation0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 0, 20 }
                }
                BirthRotationalVelocity0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 0, 2040 }
                }
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 2.20000005, 2.20000005, 2.20000005 }
                }
                Texture: string = "ASSETS/Characters/Heimerdinger/Skins/Skin04/Particles/Heimerdinger_Skin04_CandyCane_TX.dds"
            }
        }
        ParticleName: string = "Heimerdinger_Skin04_AA_mis"
        ParticlePath: string = "Characters/Heimerdinger/Skins/Skin4/Particles/Heimerdinger_Skin04_AA_mis"
    }
    "Characters/Heimerdinger/Skins/Skin4/Particles/Heimerdinger_Skin04_Crit_mis" = VfxSystemDefinitionData {
        ComplexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 120
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 0.5
                }
                EmitterName: string = "trail"
                Primitive: pointer = VfxPrimitiveArbitraryQuad {}
                Color: embed = ValueColor {
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            0.100000001
                            0.300000012
                            1
                        }
                        Values: list[vec4] = {
                            { 0.550000012, 0.349999994, 0.349999994, 0.25 }
                            { 0.449999988, 0.349999994, 0.349999994, 0.0500000007 }
                            { 0.349999994, 0.349999994, 0.349999994, 0.0500000007 }
                            { 0.349999994, 0.349999994, 0.349999994, 0 }
                        }
                    }
                }
                BirthRotation0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 0, 90 }
                }
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 90, 17, 17 }
                }
                Scale0: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            1
                        }
                        Values: list[vec3] = {
                            { 1, 1, 1 }
                            { 0.100000001, 0.100000001, 0.100000001 }
                        }
                    }
                }
                Texture: string = "ASSETS/Shared/Particles/AirSpiritStreak.DDS"
                StartFrame: u16 = 1
                TexDiv: vec2 = { 2, 2 }
            }
            VfxEmitterDefinitionData {
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 5
                }
                EmitterName: string = "wrench"
                Importance: u8 = 2
                BindWeight: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                Primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Heimerdinger/Skins/Skin04/Particles/heimerdinger_skin04_aa_candycane_2.scb"
                    }
                }
                BlendMode: u8 = 1
                BirthRotation0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 0, 20 }
                }
                BirthRotationalVelocity0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 0, 2040 }
                }
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 2.20000005, 2.20000005, 2.20000005 }
                }
                Texture: string = "ASSETS/Characters/Heimerdinger/Skins/Skin04/Particles/Heimerdinger_Skin04_CandyCane_TX.dds"
            }
            VfxEmitterDefinitionData {
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 5
                }
                EmitterName: string = "wrench2"
                BindWeight: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                Primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Heimerdinger/Skins/Skin04/Particles/heimerdinger_skin04_aa_candycane_2.scb"
                    }
                }
                BlendMode: u8 = 1
                BirthRotation0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 0, -50 }
                }
                BirthRotationalVelocity0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 0, 2040 }
                }
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 2.20000005, 2.20000005, 2.20000005 }
                }
                Texture: string = "ASSETS/Characters/Heimerdinger/Skins/Skin04/Particles/Heimerdinger_Skin04_CandyCane_TX.dds"
            }
            VfxEmitterDefinitionData {
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 120
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 0.5
                }
                EmitterName: string = "trail2"
                Primitive: pointer = VfxPrimitiveArbitraryQuad {}
                Color: embed = ValueColor {
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            0.100000001
                            0.300000012
                            1
                        }
                        Values: list[vec4] = {
                            { 0.550000012, 0.349999994, 0.349999994, 0.25 }
                            { 0.449999988, 0.349999994, 0.349999994, 0.0500000007 }
                            { 0.349999994, 0.349999994, 0.349999994, 0.0500000007 }
                            { 0.349999994, 0.349999994, 0.349999994, 0 }
                        }
                    }
                }
                BirthRotation0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 0, -90 }
                }
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 90, 17, 17 }
                }
                Scale0: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            1
                        }
                        Values: list[vec3] = {
                            { 1, 1, 1 }
                            { 0.100000001, 0.100000001, 0.100000001 }
                        }
                    }
                }
                Texture: string = "ASSETS/Shared/Particles/AirSpiritStreak.DDS"
                StartFrame: u16 = 1
                TexDiv: vec2 = { 2, 2 }
            }
        }
        ParticleName: string = "Heimerdinger_Skin04_Crit_mis"
        ParticlePath: string = "Characters/Heimerdinger/Skins/Skin4/Particles/Heimerdinger_Skin04_Crit_mis"
    }
    "Characters/Heimerdinger/Skins/Skin4/Particles/Heimerdinger_Skin04_AA_2_mis" = VfxSystemDefinitionData {
        ComplexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 120
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 0.5
                }
                EmitterName: string = "trail"
                Primitive: pointer = VfxPrimitiveArbitraryQuad {}
                Color: embed = ValueColor {
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            0.100000001
                            0.300000012
                            1
                        }
                        Values: list[vec4] = {
                            { 0.550000012, 0.349999994, 0.349999994, 0.25 }
                            { 0.449999988, 0.349999994, 0.349999994, 0.0500000007 }
                            { 0.349999994, 0.349999994, 0.349999994, 0.0500000007 }
                            { 0.349999994, 0.349999994, 0.349999994, 0 }
                        }
                    }
                }
                BirthRotation0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 0, 90 }
                }
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 90, 17, 17 }
                }
                Scale0: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            1
                        }
                        Values: list[vec3] = {
                            { 1, 1, 1 }
                            { 0.100000001, 0.100000001, 0.100000001 }
                        }
                    }
                }
                Texture: string = "ASSETS/Shared/Particles/AirSpiritStreak.DDS"
                StartFrame: u16 = 1
                TexDiv: vec2 = { 2, 2 }
            }
            VfxEmitterDefinitionData {
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 5
                }
                EmitterName: string = "candycane"
                Importance: u8 = 2
                BindWeight: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                Primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Heimerdinger/Skins/Skin04/Particles/heimerdinger_skin04_aa_candycane_2.scb"
                    }
                }
                BlendMode: u8 = 1
                BirthRotation0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 0, 20 }
                }
                BirthRotationalVelocity0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 0, 2040 }
                }
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 2.20000005, 2.20000005, 2.20000005 }
                }
                Texture: string = "ASSETS/Characters/Heimerdinger/Skins/Skin04/Particles/Heimerdinger_Skin04_CandyCane_TX.dds"
            }
        }
        ParticleName: string = "Heimerdinger_Skin04_AA_2_mis"
        ParticlePath: string = "Characters/Heimerdinger/Skins/Skin4/Particles/Heimerdinger_Skin04_AA_2_mis"
    }
}
