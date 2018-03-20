parameters, tasks, modules, agents, levels = [], [], [], [], []
filename_work = "C:\Tecom\Qligent\RCA\gen\RCA.config"
filename_home = "C:\RCA.config"

agents_list = {"KV": "m7-ql-bks01",
               "ML": "m7-ql-bks02",
               "MD": "m7-ql-bks03",
               "NN": "m7-ql-bks04",
               "ON": "m7-ql-bks05",
               "PZ": "m7-ql-bks06",
               "SM": "m7-ql-bks07",
               "SR": "m7-ql-bks08",
               "UD": "m7-ql-bks09",
               "UL": "m7-ql-bks10",
               "CH": "m7-ql-bks11",
               "TT": "m7-ql-bks12",
               "Probe": "probe1cbba8ffff18"}

#modules_list = ["SNMPMonitor"]
tasks_list = ["VLG-NNOV-MRF SIB.FED.028.SD4.TS1",
              "VLG-NNOV-RF SZF.FED.032.SD4.0S1", "VLG-NNOV2-MRF SZF.FED.956.HD4.0S1"]   #"MLR", "NoSignal", "BitratePeak"
params_list = {"SNMPMonitor": ["IAT"],
               "IPStatistics": ["averageJitter", "mediaLossRate", "mediaLossTotal"],
               "MpegTSStatisticsIPTVControlModule": ["overallBitrate"],
               "TR101290": ["Continuity_count_err"]}


alertType = "qos.RCA.testChanelNN"
originatorId = 1522072
config_name = "Test RCA NN channels"
rule = ["L2"]
originatorId_name = "originatorId"
alertTypeName = "alertTypeName"
taskKey_name = "taskKey"
levels_name = "levels"
rcaSeverity_name = "rcaSeverity"
rules_name = "rules"
name = "name"
priority_name = "priority"
parameters_name = "parameters"
tasks_name = "tasks"
key_name = "key"
agents_name = "agents"
modules_name = "modules"
