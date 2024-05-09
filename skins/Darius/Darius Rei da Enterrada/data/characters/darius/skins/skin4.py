#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {
    "DATA/Darius_Skins_Skin10_Skins_Skin11_Skins_Skin12_Skins_Skin13_Skins_Skin4_Skins_Skin53_Skins_Skin9.bin"
    "DATA/Darius_Skins_Skin0_Skins_Skin1_Skins_Skin10_Skins_Skin11_Skins_Skin12_Skins_Skin13_Skins_Skin14_Skins_Skin15_Skins_Skin16_Skins_Skin17_Skins_Skin18_Skins_Skin19_Skins_Skin2_Skins_Skin20_Skins_Skin21_Skins_Skin22_Skins_Skin23_Skins_Skin3_Skins_Skin4_Skins_Skin5_Skins_Skin53_Skins_Skin6_Skins_Skin7_Skins_Skin8_Skins_Skin9.bin"
    "DATA/Characters/Darius/Darius.bin"
    "DATA/Darius_Skins_Skin0_Skins_Skin1_Skins_Skin10_Skins_Skin11_Skins_Skin12_Skins_Skin13_Skins_Skin14_Skins_Skin15_Skins_Skin2_Skins_Skin3_Skins_Skin4_Skins_Skin5_Skins_Skin53_Skins_Skin6_Skins_Skin7_Skins_Skin8_Skins_Skin9.bin"
    "DATA/Characters/Darius/Animations/Skin4.bin"
    "DATA/Darius_Skins_Skin0_Skins_Skin1_Skins_Skin10_Skins_Skin11_Skins_Skin12_Skins_Skin13_Skins_Skin16_Skins_Skin17_Skins_Skin18_Skins_Skin19_Skins_Skin2_Skins_Skin20_Skins_Skin21_Skins_Skin22_Skins_Skin23_Skins_Skin3_Skins_Skin4_Skins_Skin5_Skins_Skin53_Skins_Skin6_Skins_Skin7_Skins_Skin8_Skins_Skin9.bin"
    "DATA/Darius_Skins_Skin0_Skins_Skin1_Skins_Skin10_Skins_Skin11_Skins_Skin12_Skins_Skin13_Skins_Skin14_Skins_Skin15_Skins_Skin16_Skins_Skin17_Skins_Skin18_Skins_Skin19_Skins_Skin2_Skins_Skin20_Skins_Skin21_Skins_Skin22_Skins_Skin23_Skins_Skin3_Skins_Skin33_Skins_Skin34_Skins_Skin35_Skins_Skin36_Skins_Skin37_Skins_Skin38_Skins_Skin39_Skins_Skin4_Skins_Skin40_Skins_Skin41_Skins_Skin42_Skins_Skin5_Skins_Skin53_Skins_Skin6_Skins_Skin7_Skins_Skin8_Skins_Skin9.bin"
    "DATA/Darius_Skins_Skin0_Skins_Skin1_Skins_Skin10_Skins_Skin11_Skins_Skin12_Skins_Skin13_Skins_Skin14_Skins_Skin16_Skins_Skin17_Skins_Skin18_Skins_Skin19_Skins_Skin2_Skins_Skin20_Skins_Skin21_Skins_Skin22_Skins_Skin23_Skins_Skin3_Skins_Skin33_Skins_Skin34_Skins_Skin35_Skins_Skin36_Skins_Skin37_Skins_Skin38_Skins_Skin39_Skins_Skin4_Skins_Skin40_Skins_Skin41_Skins_Skin42_Skins_Skin5_Skins_Skin53_Skins_Skin6_Skins_Skin7_Skins_Skin8_Skins_Skin9.bin"
    "DATA/Darius_Skins_Skin0_Skins_Skin1_Skins_Skin10_Skins_Skin11_Skins_Skin12_Skins_Skin13_Skins_Skin2_Skins_Skin3_Skins_Skin4_Skins_Skin5_Skins_Skin53_Skins_Skin6_Skins_Skin7_Skins_Skin8_Skins_Skin9.bin"
    "DATA/Darius_Skins_Skin10_Skins_Skin11_Skins_Skin12_Skins_Skin13_Skins_Skin4_Skins_Skin9.bin"
    "DATA/Darius_Skins_Skin4_Skins_Skin53.bin"
}
entries: map[hash,embed] = {
    "Characters/Darius/Skins/Skin0" = SkinCharacterDataProperties {
        SkinClassification: u32 = 1
        ChampionSkinName: string = "DariusSkin04"
        MetaDataTags: string = "faction:noxus,gender:male,race:human,skinline:dunkmaster"
        Loadscreen: embed = CensoredImage {
            Image: string = "ASSETS/Characters/Darius/Skins/Skin04/DariusLoadScreen_4.dds"
        }
        SkinAudioProperties: embed = SkinAudioProperties {
            TagEventList: list[string] = {
                "Darius"
                "DariusSkin04"
            }
            BankUnits: list2[embed] = {
                BankUnit {
                    Name: string = "Darius_Base_SFX"
                    BankPath: list[string] = {
                        "ASSETS/Sounds/Wwise2016/SFX/Characters/Darius/Skins/Base/Darius_Base_SFX_audio.bnk"
                        "ASSETS/Sounds/Wwise2016/SFX/Characters/Darius/Skins/Base/Darius_Base_SFX_events.bnk"
                    }
                }
                BankUnit {
                    Name: string = "Darius_Skin04_VO"
                    BankPath: list[string] = {
                        "ASSETS/Sounds/Wwise2016/VO/en_US/Characters/Darius/Skins/Skin04/Darius_Skin04_VO_audio.bnk"
                        "ASSETS/Sounds/Wwise2016/VO/en_US/Characters/Darius/Skins/Skin04/Darius_Skin04_VO_events.bnk"
                        "ASSETS/Sounds/Wwise2016/VO/en_US/Characters/Darius/Skins/Skin04/Darius_Skin04_VO_audio.wpk"
                    }
                    Events: list[string] = {
                        "Play_vo_DariusSkin04_Attack2DGeneral"
                        "Play_vo_DariusSkin04_BuyItem2DBloodthirster"
                        "Play_vo_DariusSkin04_BuyItem2DBoots"
                        "Play_vo_DariusSkin04_BuyItem2DInfinityEdge"
                        "Play_vo_DariusSkin04_BuyItem2DMawofMalmortius"
                        "Play_vo_DariusSkin04_BuyItem2DRanduinsOmen"
                        "Play_vo_DariusSkin04_BuyItem2DRavenousHydra"
                        "Play_vo_DariusSkin04_BuyItem2DStrideBreaker"
                        "Play_vo_DariusSkin04_BuyItem2DSunfireAegis"
                        "Play_vo_DariusSkin04_BuyItem2DTrinityForce"
                        "Play_vo_DariusSkin04_DariusAxeGrabCone_cast3D"
                        "Play_vo_DariusSkin04_DariusBasicAttack2_cast3D"
                        "Play_vo_DariusSkin04_DariusBasicAttack_cast3D"
                        "Play_vo_DariusSkin04_DariusCleave_cast3D"
                        "Play_vo_DariusSkin04_DariusCritAttack_cast3D"
                        "Play_vo_DariusSkin04_DariusExecute_cast3D"
                        "Play_vo_DariusSkin04_DariusNoxianTacticsONHAttack_cast3D"
                        "Play_vo_DariusSkin04_Death3D"
                        "Play_vo_DariusSkin04_FirstEncounter3DAmumu"
                        "Play_vo_DariusSkin04_FirstEncounter3DAshe"
                        "Play_vo_DariusSkin04_FirstEncounter3DBrand"
                        "Play_vo_DariusSkin04_FirstEncounter3DCaitlyn"
                        "Play_vo_DariusSkin04_FirstEncounter3DDiana"
                        "Play_vo_DariusSkin04_FirstEncounter3DDraven"
                        "Play_vo_DariusSkin04_FirstEncounter3DDrMundo"
                        "Play_vo_DariusSkin04_FirstEncounter3DEzreal"
                        "Play_vo_DariusSkin04_FirstEncounter3DFiddlesticks"
                        "Play_vo_DariusSkin04_FirstEncounter3DGangplank"
                        "Play_vo_DariusSkin04_FirstEncounter3DGaren"
                        "Play_vo_DariusSkin04_FirstEncounter3DGeneral"
                        "Play_vo_DariusSkin04_FirstEncounter3DGragas"
                        "Play_vo_DariusSkin04_FirstEncounter3DJanna"
                        "Play_vo_DariusSkin04_FirstEncounter3DLeeSin"
                        "Play_vo_DariusSkin04_FirstEncounter3DLeona"
                        "Play_vo_DariusSkin04_FirstEncounter3DLulu"
                        "Play_vo_DariusSkin04_FirstEncounter3DMalphite"
                        "Play_vo_DariusSkin04_FirstEncounter3DMaokai"
                        "Play_vo_DariusSkin04_FirstEncounter3DMasterYi"
                        "Play_vo_DariusSkin04_FirstEncounter3DNocturne"
                        "Play_vo_DariusSkin04_FirstEncounter3DOrianna"
                        "Play_vo_DariusSkin04_FirstEncounter3DRammus"
                        "Play_vo_DariusSkin04_FirstEncounter3DSion"
                        "Play_vo_DariusSkin04_FirstEncounter3DSona"
                        "Play_vo_DariusSkin04_FirstEncounter3DSoraka"
                        "Play_vo_DariusSkin04_FirstEncounter3DTrundle"
                        "Play_vo_DariusSkin04_FirstEncounter3DUdyr"
                        "Play_vo_DariusSkin04_FirstEncounter3DVi"
                        "Play_vo_DariusSkin04_FirstEncounter3DVladimir"
                        "Play_vo_DariusSkin04_FirstEncounter3DZilean"
                        "Play_vo_DariusSkin04_FirstEncounter3DZyra"
                        "Play_vo_DariusSkin04_Joke3DGeneral"
                        "Play_vo_DariusSkin04_Laugh3DGeneral"
                        "Play_vo_DariusSkin04_Move2DFirst"
                        "Play_vo_DariusSkin04_Move2DStandard"
                        "Play_vo_DariusSkin04_Recall3DGeneral"
                        "Play_vo_DariusSkin04_Respawn2DGeneral"
                        "Play_vo_DariusSkin04_Spell3DPMax"
                        "Play_vo_DariusSkin04_Taunt3DGeneral"
                        "Play_vo_DariusSkin04_UseItem2DWard"
                    }
                    VoiceOver: bool = true
                }
                BankUnit {
                    Name: string = "Darius_Skin04_SFX"
                    BankPath: list[string] = {
                        "ASSETS/Sounds/Wwise2016/SFX/Characters/Darius/Skins/Skin04/Darius_Skin04_SFX_audio.bnk"
                        "ASSETS/Sounds/Wwise2016/SFX/Characters/Darius/Skins/Skin04/Darius_Skin04_SFX_events.bnk"
                    }
                    Events: list[string] = {
                        "Play_sfx_DariusSkin04_Dance3D_buffactivate"
                        "Play_sfx_DariusSkin04_Dance3D_loop"
                        "Play_sfx_DariusSkin04_DariusAxeGrabCone_OnCast"
                        "Play_sfx_DariusSkin04_DariusAxeGrabCone_OnHit"
                        "Play_sfx_DariusSkin04_DariusAxeGrabConeBump_buffactivate"
                        "Play_sfx_DariusSkin04_DariusBasicAttack2_OnCast"
                        "Play_sfx_DariusSkin04_DariusBasicAttack2_OnHit"
                        "Play_sfx_DariusSkin04_DariusBasicAttack_OnCast"
                        "Play_sfx_DariusSkin04_DariusBasicAttack_OnHit"
                        "Play_sfx_DariusSkin04_DariusCleave_hit_inner"
                        "Play_sfx_DariusSkin04_DariusCleave_hit_outter"
                        "Play_sfx_DariusSkin04_DariusCleave_OnCast"
                        "Play_sfx_DariusSkin04_DariusCritAttack_OnCast"
                        "Play_sfx_DariusSkin04_DariusCritAttack_OnHit"
                        "Play_sfx_DariusSkin04_DariusExecute_hit_kill"
                        "Play_sfx_DariusSkin04_DariusExecute_OnCast"
                        "Play_sfx_DariusSkin04_DariusExecute_OnHit"
                        "Play_sfx_DariusSkin04_DariusHemoMax_loop"
                        "Play_sfx_DariusSkin04_DariusHemoMax_OnBuffActivate"
                        "Play_sfx_DariusSkin04_DariusNoxianTacticsONH_OnBuffActivate"
                        "Play_sfx_DariusSkin04_DariusNoxianTacticsONH_OnBuffDeactivate"
                        "Play_sfx_DariusSKin04_DariusNoxianTacticsONH_OnCast"
                        "Play_sfx_DariusSkin04_DariusNoxianTacticsONHAttack_OnCast"
                        "Play_sfx_DariusSkin04_DariusNoxianTacticsONHAttack_OnHit"
                        "Play_sfx_DariusSkin04_DariusQCast_OnBuffDeactivate"
                        "Play_sfx_DariusSkin04_Death3D_cast"
                        "Play_sfx_DariusSkin04_Joke3D_buffactivate"
                        "Play_sfx_DariusSkin04_Laugh3D_buffactivate"
                        "Play_sfx_DariusSkin04_Recall_leadin"
                        "Play_sfx_DariusSkin04_Recall_leadout1"
                        "Play_sfx_DariusSkin04_Recall_leadout2"
                        "Play_sfx_DariusSkin04_Respawn_buffactivate"
                        "Play_sfx_DariusSkin04_Taunt3D_buffactivate"
                        "Stop_sfx_DariusSkin04_Dance3D_buffactivate"
                        "Stop_sfx_DariusSkin04_Dance3D_loop"
                        "Stop_sfx_DariusSkin04_DariusHemoMax_loop"
                        "Stop_sfx_DariusSkin04_DariusNoxianTacticsONH_OnBuffActivate"
                        "Stop_sfx_DariusSkin04_Death3D_cast"
                        "Stop_sfx_DariusSkin04_Joke3D_buffactivate"
                        "Stop_sfx_DariusSkin04_Laugh3D_buffactivate"
                        "Stop_sfx_DariusSkin04_Recall_leadin"
                        "Stop_sfx_DariusSkin04_Recall_leadout1"
                        "Stop_sfx_DariusSkin04_Recall_leadout2"
                        "Stop_sfx_DariusSkin04_Respawn_buffactivate"
                        "Stop_sfx_DariusSkin04_Taunt3D_buffactivate"
                    }
                }
            }
        }
        SkinAnimationProperties: embed = SkinAnimationProperties {
            AnimationGraphData: link = "Characters/Darius/Animations/Skin4"
        }
        SkinMeshProperties: embed = SkinMeshDataProperties {
            Skeleton: string = "ASSETS/Characters/Darius/Skins/Skin04/Darius_Skin04.skl"
            SimpleSkin: string = "ASSETS/Characters/Darius/Skins/Skin04/Darius_Skin04.skn"
            Texture: string = "ASSETS/Characters/Darius/Skins/Skin04/Darius_Skin04_TX_CM.dds"
            GlossTexture: string = "ASSETS/Characters/Darius/Skins/Skin04/Darius_Skin04_TX_GM.dds"
            SkinScale: f32 = 1.04999995
            SelfIllumination: f32 = 0.699999988
            BrushAlphaOverride: f32 = 0.550000012
            OverrideBoundingBox: option[vec3] = {
                { 120, 250, 120 }
            }
            FresnelColor: rgba = { 26, 56, 64, 255 }
            Fresnel: f32 = 0.100000001
            UsesSkinVo: bool = true
            ReflectionMap: string = "ASSETS/Characters/Darius/Skins/Skin04/Darius_Skin04_CubeMap.dds"
            ReflectionOpacityDirect: f32 = 0.699999988
            ReflectionFresnel: f32 = 0.100000001
            ReflectionFresnelColor: rgba = { 26, 26, 26, 255 }
        }
        ArmorMaterial: string = "Flesh"
        IconAvatar: string = "ASSETS/Characters/Darius/HUD/Darius_Circle_4.dds"
        mContextualActionData: link = "Characters/Darius/CAC/Darius_Skin04"
        IconCircle: option[string] = {
            "ASSETS/Characters/Darius/HUD/Darius_Circle_0.dds"
        }
        IconSquare: option[string] = {
            "ASSETS/Characters/Darius/HUD/Darius_Square_0.dds"
        }
        HealthBarData: embed = CharacterHealthBarDataRecord {
            UnitHealthBarStyle: u8 = 10
        }
        mEmblems: list[embed] = {
            SkinEmblem {
                mEmblemData: link = "Emblems/31"
            }
        }
        mResourceResolver: link = "Characters/Darius/Skins/Skin4/Resources"
    }
"Characters/Darius/Skins/Skin0/Resources" = ResourceResolver {
        ResourceMap: map[hash,link] = {
            0xde8f77d1 = "Characters/Darius/Skins/Skin0/Particles/BloodSlash"
            "Darius_BA" = "Characters/Darius/Skins/Skin4/Particles/Darius_Skin04_BA"
            "Darius_BA2" = "Characters/Darius/Skins/Skin4/Particles/Darius_Skin04_BA"
            "Darius_BA_Crit" = "Characters/Darius/Skins/Skin4/Particles/Darius_Skin04_BA_Crit"
            "Darius_E_Axegrab_Collision" = "Characters/Darius/Skins/Skin4/Particles/Darius_Skin04_E_Axegrab_Collision"
            "Darius_E_tar" = "Characters/Darius/Skins/Skin4/Particles/darius_Skin04_E_tar"
            "Darius_E_tar_02" = "Characters/Darius/Skins/Skin4/Particles/darius_Skin04_E_tar_02"
            "Darius_E_Tar_Unit_Trail" = "Characters/Darius/Skins/Skin4/Particles/Darius_Skin04_E_Tar_Unit_Trail"
            "darius_E_weapon_trigger" = "Characters/Darius/Skins/Skin4/Particles/darius_Skin04_E_weapon_trigger"
            "darius_frost_mist" = "Characters/Darius/Skins/Skin4/Particles/darius_Skin04_frost_mist"
            "darius_hemo_bleed_indicatorTalon" = "Characters/Darius/Skins/Skin0/Particles/darius_Base_hemo_bleed_indicatorTalon"
            "darius_hemo_bleed_indicator_hit" = "Characters/Darius/Skins/Skin4/Particles/darius_Skin04_hemo_bleed_indicator_hit"
            "darius_hemo_bleed_trail_only1" = "Characters/Darius/Skins/Skin4/Particles/darius_Skin04_hemo_bleed_trail_only1"
            "darius_hemo_bleed_trail_only2" = "Characters/Darius/Skins/Skin4/Particles/darius_Skin04_hemo_bleed_trail_only2"
            "darius_hemo_bleed_trail_only3" = "Characters/Darius/Skins/Skin4/Particles/darius_Skin04_hemo_bleed_trail_only3"
            "darius_hemo_bleed_trail_only4" = "Characters/Darius/Skins/Skin4/Particles/darius_Skin04_hemo_bleed_trail_only4"
            "darius_hemo_bleed_trail_only6" = "Characters/Darius/Skins/Skin4/Particles/darius_Skin04_hemo_bleed_trail_only6"
            "Darius_hemo_counter_01" = "Characters/Darius/Skins/Skin4/Particles/darius_Skin04_hemo_counter_01"
            "darius_hemo_counter_01Minion" = "Characters/Darius/Skins/Skin4/Particles/darius_Skin04_hemo_counter_01Minion"
            "Darius_hemo_counter_02" = "Characters/Darius/Skins/Skin4/Particles/darius_Skin04_hemo_counter_02"
            "darius_hemo_counter_02Minion" = "Characters/Darius/Skins/Skin4/Particles/darius_Skin04_hemo_counter_02Minion"
            "Darius_hemo_counter_03" = "Characters/Darius/Skins/Skin4/Particles/darius_Skin04_hemo_counter_03"
            "darius_hemo_counter_03Minion" = "Characters/Darius/Skins/Skin4/Particles/darius_Skin04_hemo_counter_03Minion"
            "Darius_hemo_counter_04" = "Characters/Darius/Skins/Skin4/Particles/darius_Skin04_hemo_counter_04"
            "darius_hemo_counter_04Minion" = "Characters/Darius/Skins/Skin4/Particles/darius_Skin04_hemo_counter_04Minion"
            "Darius_hemo_counter_05" = "Characters/Darius/Skins/Skin4/Particles/darius_Skin04_hemo_counter_05"
            "darius_hemo_counter_05Minion" = "Characters/Darius/Skins/Skin4/Particles/darius_Skin04_hemo_counter_05Minion"
            "Darius_passive_overhead_max_stack" = "Characters/Darius/Skins/Skin4/Particles/darius_Skin04_passive_overhead_max_stack"
            "Darius_P_axe_handle" = "Characters/Darius/Skins/Skin0/Particles/Darius_Base_P_axe_handle"
            "Darius_P_axe_tip" = "Characters/Darius/Skins/Skin4/Particles/Darius_Skin04_P_axe_tip"
            "Darius_P_enraged" = "Characters/Darius/Skins/Skin4/Particles/Darius_Skin04_P_enraged"
            "Darius_P_enraged_shoulder_L" = "Characters/Darius/Skins/Skin4/Particles/Darius_Skin04_P_enraged_shoulder_L"
            "Darius_P_enraged_shoulder_R" = "Characters/Darius/Skins/Skin4/Particles/Darius_Skin04_P_enraged_shoulder_R"
            "Darius_P_nova" = "Characters/Darius/Skins/Skin0/Particles/Darius_Base_P_nova"
            "Darius_Q_Heal" = "Characters/Darius/Skins/Skin0/Particles/Darius_Base_Q_Heal"
            "Darius_Q_Ring" = "Characters/Darius/Skins/Skin4/Particles/Darius_Skin04_Q_Ring"
            "Darius_Q_Ring_Windup" = "Characters/Darius/Skins/Skin4/Particles/Darius_Skin04_Q_Ring_Windup"
            "Darius_Q_tar" = "Characters/Darius/Skins/Skin4/Particles/darius_Skin04_Q_tar"
            "Darius_Q_tar_inner" = "Characters/Darius/Skins/Skin4/Particles/darius_Skin04_Q_tar_inner"
            "Darius_R_blood_spatter_self" = "Characters/Darius/Skins/Skin4/Particles/darius_Skin04_R_blood_spatter_self"
            "Darius_R_cast_axe" = "Characters/Darius/Skins/Skin4/Particles/darius_Skin04_R_cast_axe"
            "Darius_R_Ready" = "Characters/Darius/Skins/Skin4/Particles/Darius_Skin04_R_Ready"
            "darius_r_refresh_01" = "Characters/Darius/Skins/Skin4/Particles/darius_Skin04_r_refresh_01"
            "Darius_R_tar" = "Characters/Darius/Skins/Skin4/Particles/darius_Skin04_R_tar"
            "Darius_R_tar_02" = "Characters/Darius/Skins/Skin4/Particles/darius_Skin04_R_tar_02"
            "Darius_R_tar_03" = "Characters/Darius/Skins/Skin4/Particles/darius_Skin04_R_tar_03"
            "Darius_R_tar_04" = "Characters/Darius/Skins/Skin0/Particles/darius_Base_R_tar_04"
            "Darius_W_tar" = "Characters/Darius/Skins/Skin4/Particles/darius_Skin04_W_tar"
            "Darius_W_weapon_01" = "Characters/Darius/Skins/Skin4/Particles/darius_Skin04_W_weapon_01"
            "Darius_W_weapon_02" = "Characters/Darius/Skins/Skin4/Particles/darius_Skin04_W_weapon_02"
            "Darius_W_weapon_02_Norse_King" = "Characters/Darius/Skins/Skin4/Particles/darius_Skin04_W_weapon_02_Norse_King"
            "Darius_W_weapon_03" = "Characters/Darius/Skins/Skin4/Particles/darius_Skin04_W_weapon_03"
            "Darius_W_weapon_04" = "Characters/Darius/Skins/Skin4/Particles/darius_Skin04_W_weapon_04"
            0xec3aefb1 = "Characters/Darius/Skins/Skin0/Particles/darius_emote_dance_sound"
            0x364b9124 = "Characters/Darius/Skins/Skin0/Particles/darius_emote_death_sound"
            0xdd8a38fb = "Characters/Darius/Skins/Skin0/Particles/darius_emote_joke_sound"
            0xb9a180ba = "Characters/Darius/Skins/Skin0/Particles/darius_emote_taunt_sound"
            0x2fd2530c = "Characters/Darius/Skins/Skin0/Particles/Darius_Skin14_BA_Crit"
            0x53fa0329 = "Characters/Darius/Skins/Skin0/Particles/darius_weapon_glow_base"
            0x4e433aaf = "Characters/Darius/Skins/Skin4/Particles/darius_skin04_emote_dance_loop_sound"
            0x92bcc4e8 = "Characters/Darius/Skins/Skin4/Particles/darius_skin04_emote_dance_sound"
            0x67123a6d = "Characters/Darius/Skins/Skin4/Particles/darius_skin04_emote_death_sound"
            0x88d4fec2 = "Characters/Darius/Skins/Skin4/Particles/darius_skin04_emote_joke_sound"
            0x790c69ea = "Characters/Darius/Skins/Skin4/Particles/darius_skin04_emote_laugh_sound"
            0xe137e797 = "Characters/Darius/Skins/Skin4/Particles/darius_skin04_emote_respawn_sound"
            0xebc0a9f3 = "Characters/Darius/Skins/Skin4/Particles/darius_skin04_emote_taunt_sound"
            "Darius_Passive_Child" = "Characters/Darius/Skins/Skin4/Particles/Darius_Skin04_Passive_Child"
            "darius_Q_aoe_cast" = "Characters/Darius/Skins/Skin4/Particles/darius_Skin04_Q_aoe_cast"
            "darius_Q_aoe_cast_mist" = "Characters/Darius/Skins/Skin4/Particles/darius_Skin04_Q_aoe_cast_mist"
            "darius_Q_impact_Ring" = "Characters/Darius/Skins/Skin4/Particles/darius_Skin04_Q_impact_Ring"
            "darius_Q_impact_spray" = "Characters/Darius/Skins/Skin4/Particles/darius_Skin04_Q_impact_spray"
            0xef8f8502 = "Characters/Darius/Skins/Skin4/Particles/darius_skin04_recall_end1_sound"
            0xed082e53 = "Characters/Darius/Skins/Skin4/Particles/darius_skin04_recall_end2_sound"
            0x75927892 = "Characters/Darius/Skins/Skin4/Particles/darius_skin04_recall_start_sound"
            "darius_R_BallFire_01" = "Characters/Darius/Skins/Skin4/Particles/darius_Skin04_R_BallFire_01"
            "Darius_R_Tar_Backboard" = "Characters/Darius/Skins/Skin4/Particles/Darius_Skin04_R_Tar_Backboard"
            "Darius_W_Weapon_Child" = "Characters/Darius/Skins/Skin4/Particles/Darius_Skin04_W_Weapon_Child"
        }
    }
}
