filename_work = "C:\Tecom\Qligent\RCA\gen\RCA.config"
filename_home = "C:\RCA.config"

parameters, tasks, modules, agents, levels = [], [], [], [], []
taskKey = "VLG-NN-CBS-1.SNMPMonitor.VLG-NNOV-MRF SIB.FED.028.SD4.TS1"
alertTypeName = "qos.RCA.testChanelNN"
originatorId = 1522072

originatorId_name = "originatorId"
alertTypeName_name = "alertTypeName"
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

agents_list = ["m7-ql-bks04"]
modules_list = ["SNMPMonitor"]
tasks_list = ["VLG-NNOV-MRF SIB.FED.028.SD4.TS1",
              "VLG-NNOV-RF SZF.FED.032.SD4.0S1", "VLG-NNOV2-MRF SZF.FED.956.HD4.0S1"]   #"MLR", "NoSignal", "BitratePeak"
params_list = {"SNMPMonitor": ["IAT"],
               "IPStatistics": ["averageJitter", "mediaLossRate", "mediaLossTotal"],
               "MpegTSStatisticsIPTVControlModule": ["overallBitrate"],
               "TR101290": ["Continuity_count_err"]}
