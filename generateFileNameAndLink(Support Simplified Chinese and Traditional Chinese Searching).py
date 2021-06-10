# encoding:utf-8
# https://github.com/wangandi520/andyspythonscript

from pathlib import Path

def formatFileSize(sizeBytes):
    sizeBytes = float(sizeBytes)
    result = float(abs(sizeBytes))
    suffix = "B";
    if(result>1024):
        suffix = "KB"
        mult = 1024
        result = result / 1024
    if(result > 1024):
        suffix = "MB"
        mult *= 1024
        result = result / 1024
    if (result > 1024) :
        suffix = "GB"
        mult *= 1024
        result = result / 1024
    if (result > 1024) :
        suffix = "TB"
        mult *= 1024
        result = result / 1000
    if (result > 1024) :
        suffix = "PB"
        mult *= 1024
        result = result / 1024
    return format(result,'.2f') + suffix
        
def writefile(filereadlines):
    fileName = str(Path.cwd().name) + '.html'
    newfile = open(fileName, mode='w', encoding='UTF-8')
    newfile.writelines(filereadlines)
    newfile.close()     
    
def main():
    # 显示完整地址 = 1，还是只显示文件名 = 0
    showAllAddress = 0
    # 第一栏的宽度，first column width %
    columnWidth = 80
    # 是否显示边框，show table border = 1, no border = 0
    showTableBorder = 1
    # 是否显示第一行，show first line = 1, no first line = 0(Name, sha1, file size)
    showFirstLine = 1
    # 是否显示处理过程, show process details = 1, no detils = 0
    showProcessDetails = 1
    # 键盘按键抬起立刻搜索 = 'onkeyup'，还是按回车搜索 = 'onchange'，文件数大于两万建议后者
    howToReactSearch = 'onkeyup'
    # 相对路径 = 1，还是绝对路径 = 0
    showPath = 1
    # 显示文件夹和文件 = 1，还是只显示文件夹 = 0
    showFolderAndFile = 1
    # 是否显示文件大小，show file size = 1, no file size = 0
    showFileSize = 1
    # 点击文件夹的操作，搜索包含这个文件夹名的所有路径 = 1，跳转到这个文件夹 = 0
    clickFolder = 1
    
    title = str(Path.cwd().name)
    outputFile = '<html><head><title>' + title + '</title>\n'
    # CSS
    outputFile = outputFile + '<style>body{width:90%;}table,td{border:' + str(showTableBorder) +'px solid #000000;table-layout:fixed;border-collapse:collapse;}a{color:#000000;text-decoration: none;}td{width:10%;}table tr td:first-child{width:' + str(columnWidth) +'%;}table tr:first-child{background-color:#eee;}tr:hover{background-color:#eee;}.folder{font-weight:bold;}</style>\n'
    # Simplified Chinese and Traditional Chinese Support
    # https://github.com/mumuy/chinese-transverter
    outputFile = outputFile + '<script type="text/javascript" language="JavaScript">!function(root,factory){if(typeof module==="object"&&module.exports){module.exports=factory()}else{root.transverter=factory()}}(typeof window!=="undefined"?window:this,function(){var simplified_chinese="锕爱碍蔼皑剀嗳嫒暧瑷硙锿阂霭叆埯谙钳铵阴顸鹌腌袄奥翱嚣媪岙浇硗骜鳌罢坝钯鲅鲌摆败呗办颁绊坂辩钣帮绑镑谤岗纺报饱宝剥鲍鸨龅备贝辈钡狈惫鹎贲绷镚笔闭毕币毙哔复滗筚纰荜虑诐费赑跸铋闬鲾边变编贬辫拼笾缏鳊标镖镳飑飙骠骉鳔别鳖瘪别鳖濒宾摈滨频傧殡缤膑髌鬓并饼槟禀绠拨驳钵铂卜泼发袯钹镈饽馎鹁补扑钚钸碜财蚕残掺参惨惭灿戋浅骖鲹黪仓沧舱苍伧玱鸧艹册侧测厕帻恻栅层缯诧钗锸镲馇侪虿龇单产缠搀阐颤铲谗蝉馋刬啴冁团婵崭惮忏掸浐渐产禅胀蒇裣觇谄谶长场厂尝肠畅偿伥傥尝怅枨玚苌锠阊鲳鲿绰钞唠涛绉诌鼌车彻砗称尘沉陈衬栈榇渖谌闯龀撑诚惩骋枪柽蛏赪铛迟痴齿耻驰炽啸扦抬滞离饬鸱冲虫宠佣桩烛种冲铳丑绸筹踌畴俦帱梼诪雠处锄触橱础储厨雏憷恹绌刍诎诸蹰传创疮怆戗锤邮纯莼辁鹑缀辍镞龊词辞赐兹荠鹚从丛葱聪囱枞纵总苁骢凑薮辏窜蹿攒撺镩缞错营躜锉鹾达哒垯胆荙跶迭鞑带贷绐诒轪递隶叇骀驮担弹诞郸坛殚瘅箪赡当党挡档荡垱凼烫珰疡砀筜裆谠岛盗捣导祷焘鱽灯邓镫敌缔涤籴约莜觌诋谛适镝题点电淀颠垫巅癫钿钓调鸟粜赵轺铞鲷鸼叠谍绖轶鲽鳎钉顶订锭铤饤丢铥动东冻栋岽胨鸫斗读渎窦钭饾独镀赌犊枢椟牍笃锗阇黩断锻缎簖对队兑怼镦吨顿钝炖趸夺堕亸椭泽缍铎饳饿额鹅讹恶疴哑垭垩桠猡谔轭锇锷阏颚鳄鹗腭贰儿饵尔迩铒鲕鸸罚阀珐废酦饭烦贩范矾钒枫沨访钫鲂鳑飞诽绋绯鲱坟奋愤纷粪偾喷豮鲼风缝丰疯冯讽凤锋沣砜赗负缚赋辅妇抚辐肤讣呒绂幞赙锫韨驸鲋鳆凫麸轧夹钆该盖钙赅赶干赣秆尴绀鳡刚钢纲冈戆沟颃镐皋藁缟诰锆个搁阁鸽铬纥钾铪镉闸颌鲄给颈亘赓鲠鹒宫贡巩龚红唝够钩购构区缑觏诟钩鞴鸲顾蛊贾哌谷诂轱毂钴锢馉鲴鸪鹄鹘剐呙挂诖铦鸹哙关观馆惯贯纶掼权沦鳏鹳广扩横犷归贵轨规硅柜龟诡闺刽伪伪刿匦匮妫桧洼绘鲑鳜滚辊浑绲衮锟鲧过国锅涡划埚帼掴椁腘蜗蝈锞馃虾吓为还骇颏汉韩滩钤阚颔绗号灏胶蚝颢贺鹤呵缴蝎诃辂辖阖饸阋鹖龁鸻轰鸿纮荭讧闳闹黉后糇鲘鲎户壶护沪戏浒芦许轷鳠鹕鹱话画华哗婳桦浍狯铧骅坏怀换唤环缓欢涣焕痪奂缳锾镮阛鲩黄谎锽鳇会挥汇辉毁秽贿讳烩诲咴哕晖炜珲缋翚翙荟袆诙违阓韦颒溃荤愍缗诨阍馄伙货获祸钬镬几机鸡积记级极计挤纪际绩缉饥蓟辑剂济齐继击讥叽哜洁玑矶秸结羁蕲虮蚁觊讦迹跻霁骑骥鱾鲫鲚鹡赍齑价驾荚颊挟槚浃蛱郏铗颉见减间键贱检简歼监坚艰荐剑溅涧鉴践捡笺俭碱硷拣舰槛缄茧饯堑戬枧滥睑笕缣纤裥谏谮谫钘钱锏闲险鞯骞鳒鲣鹣咸将讲奖浆酱蒋强桨绛姜螀缰鳉脚较觉娇绞搅骄矫轿饺铰侥乔侨却学峤挢桥纠荞鲛鹪节届阶杰诫疖诘锴鲒进仅紧尽劲锦晋谨烬尽卺浕琎缙荩觐赆锓馑静惊经镜净竞径荆鲸茎痉刭弪泾烃胫迳陉靓颕垧滢荧颎蓥旧厩缪阄鸠鹫举锯剧惧驹据鉅屦榉窭篓蒌讵邹锔飓鲏龃鹃绢桊锩镌隽决绝诀珏谲镢阕阙鞒骙军骏钧匀皲馂鲪开凯垲恺忾岂铠锎闿莶馅龛钪闶铐鲓颗课壳缂轲钶骒恳垦龈硁铿抠妪殴眍库裤喾圣绔夸块侩脍蒉郐鲙宽髋矿况旷圹纩诓诳贶邝亏窥馈岿愦篑聩顷壸裈阃鲲鹍阔蜡腊蓝癞镴来赖莱厉崃徕懒梾涞濑睐籁赉铼兰烂拦篮栏揽缆阑谰澜览岚廪斓榄炼褴襕镧锒阆捞劳涝络崂痨耢铑铹乐饹鳓类泪垒镭缧颣诔里礼历丽砾沥鲤励篱俪呖坜栎枥泺洒牦疠砺粝缡莅苈蓠蚀蛎里跞轹逦郦酾锂铄雳飒骊疬鳢鲡鹂俩连联练莲恋脸链敛怜帘镰涟奁娈挛殓潋琏蔹裢鲢两辆凉粮谅唡蹒辌魉疗辽镣缭钌镠鹩猎临邻鳞赁凛懔檩渗蔺躏辚领铃灵岭龄凌棂绫鲮鸰陆刘馏偻游浏绺铆锍镏飗骝鹠鹨龙拢笼聋垄咙陇咔昽胧栊泷珑眬砻茏庞楼搂娄喽嵝溇瘘耧蝼镂髅录炉卢鲁卤颅庐掳绿虏赂禄噜垆撸摅橹栌氇渌滤泸箓胪舻辘轳镥鲈鹭鸬乱滦峦孪栾脔銮鸾药锊论轮抡伦仑囵罗锣骡箩萝骆逻啰椤烁荦脶镙驴闾榈吕侣铝屡缕褛稆吗妈马骂码玛蚂么么唛嬷杩犸蓦买卖迈麦脉劢荬满瞒蛮馒谩缦螨颟鳗鹲猫贸锚没务没镁霉谜鹛门们闷懑扪焖钔梦锰黾觅弥幂纟沵猕祢芈谧绵缅渑腼面庙纱缈鹋灭闽悯珉闵鳘鸣铭谬万殁无袜谟镆馍谋亩钼纳钠内镎难摊哝馕闹脑恼挠垴桡蛲铙讷馁拟腻泞滠鲵捻撵辇辗鲇酿袅茑镍聂镊啮嗫摄谂蹑陧颞宁拧柠狞咛宁聍苎纽钮浓农脓侬秾驽疟诺傩钕呕欧鸥沤怄瓯纡讴盘丬抛疱狍赔辔鹏苹罴铍骗谝骈飘朴缥贫嫔颦凭评鲆颇钋钷铺谱镤镨气启弃凄栖脐讫启桤渍碛绮蛴锜颀骐鲯鳍牵签铅钎迁谴谦潜佥悭椠缱羟肷荨鹐墙抢呛蔷嫱庆樯炝襁亲跄锖锵镪翘锹窍硚窑缲诮谯跷铫窃惬箧锲寝钦吣嵚揿骎请轻氢倾庼苘鲭穷琼茕巯虬赇鳅趋驱躯龋岖组觑阒驺劝颧绻诠铨鳈确鹊悫让镶饶绕扰娆荛热认韧纫纴讱轫饪驲绒荣镕嵘缛蝾颂铷颥软锐绥润闰萨杀钑赛鳃伞毵糁馓丧颡扫骚缫鳋涩啬穑铯厦赊鲨晒筛术闪删陕缮姗讪钐骟鳝鳣伤赏汤殇绱觞烧绍绡设慑畲厍叶谁婶肾审绅瘆诜声绳胜时师试识驶势释饰狮视实湿诗尸嘘埘浉绎莳谥贳轼铈铊鲺鲥鸤兽寿绶书树数输属赎竖纾纻镯鹬帅闩双骦鹴税说顺硕丝饲咝厮缌蛳锶飔饴驷鸶耸诵怂讼松擞锼飕馊诉苏肃缩稣谡骕鹔岁随虽谇孙损笋狲荪锁琐唢牺献獭挞沓阘闼态钛鲐谈叹贪瘫谭昙赕钽锬镗铴饧讨绦绦绹鼗韬职铽腾誊体锑屉绨缇跃锡鳀鹈觍阗条鲦龆铁贴听厅颋铜统恸鲖头绣谕图涂秃钍专抟砖颓蜕脱饨鲀驼鸵箨萚饦鼍娲污腽弯湾顽塆纨绾苋网辋为围伟卫维谓潍纬苇遗帏沩涠玮猬诿闱韪喂鲔鳂问闻稳温纹愠缊蕴辒阌韫鳁瓮鹟窝卧挝癯莴龌雾误钨呜吴乌诬芜坞于妩庑御怃邬铻骛鹀鹉鹜龉细袭习铣系屃玺绤胁觋诶郄饻饩鳛峡狭侠煅硖线县现显闲鲜衔锨贤宪羡娴岘崄挦猃狝痫籼藓蚬跹轩鹇项响乡厢详缃芗饷飨骧鲞销萧晓哓枭泶潇箫蟏骁鸮写谢泻协谐携撷绁缬亵锌寻衅兴慭镡荥铏骍汹讻诇锈馐鸺须虚续叙绪吁溆诩谞顼选悬绚癣碹璇谖铉镟馔峃嚯鳕讯训驯逊勋询埙浔鲟压鸭亚鸦讶厌娅挜札氩痖烟盐严验艳阉砚彦谚颜阎俨兖厣滟檐觃讠谳赝这酽闫靥颜餍魇黡鼹龂样养扬痒杨阳鸯旸炀锳钖飏摇谣遥瑶尧钥峣犹飖鳐鹞业爷页晔烨谒邺铘余馌亿医仪异译彝谊艺颐忆义诣议铱勚呓峄怿择瘗祎缢舣贻钇镒镱驿鹢鹝鹥银饮隐荫瘾铟骃应蝇赢鹰颖莹婴樱缨萤嘤茔撄颍潆璎瘿绬萦罂鸴莺鹦哟涌拥咏踊痈镛颙鲬鳙优铀忧诱莸铕鱿鲉与鱼语狱渔誉娱舆屿预驭俣伛嵛欤滪玙蓣觎谀钰阈饫郁鹆远员圆愿园缘渊鸳辕橼贠陨鸢鹓鼋阅岳悦粤彟钺云运晕韵酝郧恽殒氲涢纭赟郓杂扎臜灾载暂赞瓒赞趱錾脏赃脏驵灶枣凿唣则责啧箦谪赜贼鲗赠综锃诈铡咤揸鲊鲝齄债斋战盏毡绽斩谵飐骣鹯张帐涨账诏钊蛰辙詟辄鹧鸷阵镇针诊贞侦桢浈祯纼缜赈轸鸩帧睁争挣证郑狰峥筝诤钲铮纸质帜织执挚掷栀栉絷制觯志贽跖踯踬轵轾铚只骘钟肿众终冢众钟皱轴昼骤纣荮诹赒辀猪筑贮铸嘱驻瞩诛伫槠橥潴铢转赚啭颛装庄壮状妆坠锥赘缒骓谆准浊诼资咨眦缁谘赀辎锱镃鲻踪偬骔鲰诅钻缵鳟";var traditional_chinese="錒愛礙藹皚剴噯嬡曖璦磑鎄閡靄靉垵諳鉗銨陰頇鵪醃襖奧翺囂媼嶴澆磽驁鼇罷壩鈀鮁鮊擺敗唄辦頒絆阪辯鈑幫綁鎊謗崗紡報飽寶剝鮑鴇齙備貝輩鋇狽憊鵯賁繃鏰筆閉畢幣斃嗶複潷篳紕蓽慮詖費贔蹕鉍閈鰏邊變編貶辮拚籩緶鯿標鏢鑣颮飆驃驫鰾別鼈癟彆鱉瀕賓擯濱頻儐殯繽臏髕鬢並餅檳稟綆撥駁缽鉑蔔潑發襏鈸鎛餑餺鵓補撲鈈鈽磣財蠶殘摻參慘慚燦戔淺驂鯵黲倉滄艙蒼傖瑲鶬艸冊側測廁幘惻柵層繒詫釵鍤鑔餷儕蠆齜單産纏攙闡顫鏟讒蟬饞剗嘽囅團嬋嶄憚懺撣滻漸產禪脹蕆襝覘諂讖長場廠嘗腸暢償倀儻嚐悵棖瑒萇錩閶鯧鱨綽鈔嘮濤縐謅鼂車徹硨稱塵沈陳襯棧櫬瀋諶闖齔撐誠懲騁槍檉蟶赬鐺遲癡齒恥馳熾嘯扡擡滯離飭鴟沖蟲寵傭樁燭種衝銃醜綢籌躊疇儔幬檮譸讎處鋤觸櫥礎儲廚雛怵懨絀芻詘諸躕傳創瘡愴戧錘郵純蓴輇鶉綴輟鏃齪詞辭賜茲薺鶿從叢蔥聰囪樅縱總蓯驄湊藪輳竄躥攢攛鑹縗錯營躦銼鹺達噠墶膽薘躂叠韃帶貸紿詒軑遞隸靆駘馱擔彈誕鄲壇殫癉簞贍當黨擋檔蕩壋氹燙璫瘍碭簹襠讜島盜搗導禱燾魛燈鄧鐙敵締滌糴約蓧覿詆諦適鏑題點電澱顛墊巔癲鈿釣調鳥糶趙軺銱鯛鵃疊諜絰軼鰈鰨釘頂訂錠鋌飣丟銩動東凍棟崠腖鶇鬥讀瀆竇鈄餖獨鍍賭犢樞櫝牘篤鍺闍黷斷鍛緞籪對隊兌懟鐓噸頓鈍燉躉奪墮嚲橢澤綞鐸飿餓額鵝訛惡屙啞埡堊椏玀諤軛鋨鍔閼顎鱷鶚齶貳兒餌爾邇鉺鮞鴯罰閥琺廢醱飯煩販範礬釩楓渢訪鈁魴鰟飛誹紼緋鯡墳奮憤紛糞僨噴豶鱝風縫豐瘋馮諷鳳鋒灃碸賵負縛賦輔婦撫輻膚訃嘸紱襆賻錇韍駙鮒鰒鳧麩軋夾釓該蓋鈣賅趕幹贛稈尷紺鱤剛鋼綱岡戇溝頏鎬臯槁縞誥鋯個擱閣鴿鉻紇鉀鉿鎘閘頜魺給頸亙賡鯁鶊宮貢鞏龔紅嗊夠鈎購構區緱覯詬鉤韝鴝顧蠱賈呱穀詁軲轂鈷錮餶鯝鴣鵠鶻剮咼掛詿銛鴰噲關觀館慣貫綸摜權淪鰥鸛廣擴橫獷歸貴軌規矽櫃龜詭閨劊僞偽劌匭匱媯檜窪繪鮭鱖滾輥渾緄袞錕鯀過國鍋渦劃堝幗摑槨膕蝸蟈錁餜蝦嚇為還駭頦漢韓灘鈐闞頷絎號灝膠蠔顥賀鶴嗬繳蠍訶輅轄闔餄鬩鶡齕鴴轟鴻紘葒訌閎鬨黌後餱鮜鱟戶壺護滬戲滸蘆許軤鱯鶘鸌話畫華嘩嫿樺澮獪鏵驊壞懷換喚環緩歡渙煥瘓奐繯鍰鐶闤鯇黃謊鍠鰉會揮匯輝毀穢賄諱燴誨噅噦暉煒琿繢翬翽薈褘詼違闠韋頮潰葷湣緡諢閽餛夥貨獲禍鈥鑊幾機雞積記級極計擠紀際績緝饑薊輯劑濟齊繼擊譏嘰嚌潔璣磯稭結羈蘄蟣蟻覬訐跡躋霽騎驥魢鯽鱭鶺齎齏價駕莢頰挾檟浹蛺郟鋏頡見減間鍵賤檢簡殲監堅艱薦劍濺澗鑒踐撿箋儉堿鹼揀艦檻緘繭餞塹戩梘濫瞼筧縑纖襇諫譖譾鈃錢鐧閒險韉騫鰜鰹鶼鹹將講獎漿醬蔣強槳絳薑螿韁鱂腳較覺嬌絞攪驕矯轎餃鉸僥喬僑卻學嶠撟橋糾蕎鮫鷦節屆階傑誡癤詰鍇鮚進僅緊盡勁錦晉謹燼儘巹濜璡縉藎覲贐鋟饉靜驚經鏡淨競徑荊鯨莖痙剄弳涇烴脛逕陘靚頴坰瀅熒熲鎣舊廄繆鬮鳩鷲舉鋸劇懼駒據钜屨櫸窶簍蔞詎鄒鋦颶鮍齟鵑絹棬錈鐫雋決絕訣玨譎钁闋闕鞽騤軍駿鈞勻皸餕鮶開凱塏愷愾豈鎧鐦闓薟餡龕鈧閌銬鮳顆課殼緙軻鈳騍懇墾齦硜鏗摳嫗毆瞘庫褲嚳聖絝誇塊儈膾蕢鄶鱠寬髖礦況曠壙纊誆誑貺鄺虧窺饋巋憒簣聵頃壼褌閫鯤鶤闊蠟臘藍癩鑞來賴萊厲崍徠懶棶淶瀨睞籟賚錸蘭爛攔籃欄攬纜闌讕瀾覽嵐廩斕欖煉襤襴鑭鋃閬撈勞澇絡嶗癆耮銠鐒樂餎鰳類淚壘鐳縲纇誄裏禮曆麗礫瀝鯉勵籬儷嚦壢櫟櫪濼灑犛癘礪糲縭蒞藶蘺蝕蠣裡躒轢邐酈釃鋰鑠靂颯驪鬁鱧鱺鸝倆連聯練蓮戀臉鏈斂憐簾鐮漣奩孌攣殮瀲璉蘞褳鰱兩輛涼糧諒啢蹣輬魎療遼鐐繚釕鏐鷯獵臨鄰鱗賃凜懍檁滲藺躪轔領鈴靈嶺齡淩欞綾鯪鴒陸劉餾僂遊瀏綹鉚鋶鎦飀騮鶹鷚龍攏籠聾壟嚨隴哢曨朧櫳瀧瓏矓礱蘢龐樓摟婁嘍嶁漊瘺耬螻鏤髏錄爐盧魯鹵顱廬擄綠虜賂祿嚕壚擼攄櫓櫨氌淥濾瀘籙臚艫轆轤鑥鱸鷺鸕亂灤巒孿欒臠鑾鸞藥鋝論輪掄倫侖圇羅鑼騾籮蘿駱邏囉欏爍犖腡鏍驢閭櫚呂侶鋁屢縷褸穭嗎媽馬罵碼瑪螞麼麽嘜嬤榪獁驀買賣邁麥脈勱蕒滿瞞蠻饅謾縵蟎顢鰻鸏貓貿錨冇務沒鎂黴謎鶥門們悶懣捫燜鍆夢錳黽覓彌冪糸濔獼禰羋謐綿緬澠靦麵廟紗緲鶓滅閩憫瑉閔鰵鳴銘謬萬歿無襪謨鏌饃謀畝鉬納鈉內鎿難攤噥饢鬧腦惱撓堖橈蟯鐃訥餒擬膩濘灄鯢撚攆輦輾鯰釀嫋蔦鎳聶鑷齧囁攝諗躡隉顳甯擰檸獰嚀寧聹苧紐鈕濃農膿儂穠駑瘧諾儺釹嘔歐鷗漚慪甌紆謳盤爿拋皰麅賠轡鵬蘋羆鈹騙諞駢飄樸縹貧嬪顰憑評鮃頗釙鉕鋪譜鏷鐠氣啓棄淒棲臍訖啟榿漬磧綺蠐錡頎騏鯕鰭牽簽鉛釺遷譴謙潛僉慳槧繾羥膁蕁鵮牆搶嗆薔嬙慶檣熗繈親蹌錆鏘鏹翹鍬竅礄窯繰誚譙蹺銚竊愜篋鍥寢欽唚嶔撳駸請輕氫傾廎檾鯖窮瓊煢巰虯賕鰍趨驅軀齲嶇組覷闃騶勸顴綣詮銓鰁確鵲愨讓鑲饒繞擾嬈蕘熱認韌紉紝訒軔飪馹絨榮鎔嶸縟蠑頌銣顬軟銳綏潤閏薩殺鈒賽鰓傘毿糝饊喪顙掃騷繅鰠澀嗇穡銫廈賒鯊曬篩術閃刪陝繕姍訕釤騸鱔鱣傷賞湯殤緔觴燒紹綃設懾佘厙葉誰嬸腎審紳瘮詵聲繩勝時師試識駛勢釋飾獅視實濕詩屍噓塒溮繹蒔諡貰軾鈰鉈鯴鰣鳲獸壽綬書樹數輸屬贖豎紓紵鐲鷸帥閂雙驦鸘稅說順碩絲飼噝廝緦螄鍶颸飴駟鷥聳誦慫訟鬆擻鎪颼餿訴蘇肅縮穌謖驌鷫歲隨雖誶孫損筍猻蓀鎖瑣嗩犧獻獺撻遝闒闥態鈦鮐談歎貪癱譚曇賧鉭錟鏜鐋餳討縧絛綯鞀韜職鋱騰謄體銻屜綈緹躍錫鯷鵜覥闐條鰷齠鐵貼聽廳頲銅統慟鮦頭繡諭圖塗禿釷專摶磚頹蛻脫飩魨駝鴕籜蘀飥鼉媧汙膃彎灣頑壪紈綰莧網輞爲圍偉衛維謂濰緯葦遺幃溈潿瑋蝟諉闈韙餵鮪鰃問聞穩溫紋慍縕蘊轀閿韞鰮甕鶲窩臥撾臒萵齷霧誤鎢嗚吳烏誣蕪塢於嫵廡禦憮鄔鋙騖鵐鵡鶩齬細襲習銑係屭璽綌脅覡誒郤餏餼鰼峽狹俠煆硤線縣現顯閑鮮銜鍁賢憲羨嫻峴嶮撏獫獮癇秈蘚蜆躚軒鷳項響鄉廂詳緗薌餉饗驤鯗銷蕭曉嘵梟澩瀟簫蠨驍鴞寫謝瀉協諧攜擷絏纈褻鋅尋釁興憖鐔滎鉶騂洶訩詗鏽饈鵂須虛續敘緒籲漵詡諝頊選懸絢癬镟璿諼鉉鏇饌嶨謔鱈訊訓馴遜勳詢塤潯鱘壓鴨亞鴉訝厭婭掗劄氬瘂煙鹽嚴驗豔閹硯彥諺顔閻儼兗厴灩簷覎訁讞贗這釅閆靨顏饜魘黶鼴齗樣養揚癢楊陽鴦暘煬鍈鍚颺搖謠遙瑤堯鑰嶢猶颻鰩鷂業爺頁曄燁謁鄴鋣餘饁億醫儀異譯彜誼藝頤憶義詣議銥勩囈嶧懌擇瘞禕縊艤貽釔鎰鐿驛鷁鷊鷖銀飲隱蔭癮銦駰應蠅贏鷹穎瑩嬰櫻纓螢嚶塋攖潁瀠瓔癭緓縈罌鴬鶯鸚喲湧擁詠踴癰鏞顒鯒鱅優鈾憂誘蕕銪魷鮋與魚語獄漁譽娛輿嶼預馭俁傴崳歟澦璵蕷覦諛鈺閾飫鬱鵒遠員圓願園緣淵鴛轅櫞貟隕鳶鵷黿閱嶽悅粵彠鉞雲運暈韻醞鄖惲殞氳溳紜贇鄆雜紮臢災載暫贊瓚讚趲鏨髒贓臟駔竈棗鑿唕則責嘖簀謫賾賊鰂贈綜鋥詐鍘吒摣鮓鮺齇債齋戰盞氈綻斬譫颭驏鸇張帳漲賬詔釗蟄轍讋輒鷓鷙陣鎮針診貞偵楨湞禎紖縝賑軫鴆幀睜爭掙證鄭猙崢箏諍鉦錚紙質幟織執摯擲梔櫛縶製觶誌贄蹠躑躓軹輊銍隻騭鍾腫衆終塚眾鐘皺軸晝驟紂葤諏賙輈豬築貯鑄囑駐矚誅佇櫧櫫瀦銖轉賺囀顓裝莊壯狀妝墜錐贅縋騅諄準濁諑資谘眥緇諮貲輜錙鎡鯔蹤傯騌鯫詛鑽纘鱒";simplified_chinese+="历布占恒致征折向舍千累困肮板表采杆琅狸刹台凶岩症注着锛镔铖钏镄擀睾镓钜镘麽铌鲶铩谑芸锺垅吒彷馀宁槔飚溜锘锝锪镅曲";traditional_chinese+="歷佈佔恆緻徵摺嚮捨仟纍睏骯闆錶採桿瑯貍剎臺兇巖癥註著錛鑌鋮釧鐨搟睪鎵鉅鏝麼鈮鯰鎩謔蕓鍾壠咤徬餘寧橰飈霤鍩鍀鍃鎇麯";var words={"干涸":"乾涸","计划":"計畫","台风":"颱风","度假":"渡假","头发":"頭髮","通奸":"通姦","强奸":"强姦","激荡":"激盪","复苏":"復甦"};var exception=["皇后","王后"];var zh_TW={"发布":"PO","社交网络":"社群网路","堵塞":"壅塞","缓解":"纾解","圣诞":"耶诞","熊猫":"猫熊","美女":"正妹","大爆炸":"大霹雳","水平":"水准","卫生巾":"卫生棉","风筝":"风吹","公元":"西元","公历":"西历","农历":"夏历","老幼病残孕专座":"博爱座","盒饭":"便当","一次性":"免洗","塑料瓶":"宝特瓶","热门":"夯","西伯利亚冷气团":"大陆冷气团","等离子体":"电浆","圆珠笔":"原子笔","透明皂":"水晶肥皂","洗发露":"洗发精","塑料袋":"塑胶袋","口才":"口条","人字拖":"夹脚拖","水龙头":"水喉","传统":"古早","本地":"在地","吉尼斯世界纪录":"金氏世界纪录","味精":"味素","恐怖袭击":"恐怖攻击","钥匙":"锁匙","洗面奶":"洗面乳","传统风味":"古早味","燃气灶":"瓦斯炉","创可贴":"OK绷","超声波":"超音波","激光":"脉冲光","集成电路":"积体电路","转基因":"基因改造","激光":"雷射","乒乓球":"桌球","台球":"撞球","游泳":"游水","花样游泳":"水上芭蕾","分清":"厘清","推迟":"延后","出差":"公干","纠结":"烦乱","诈骗":"诈欺","贴心":"窝心","支持":"支援","去世":"过身","幸福":"福祉","响应":"回响","前景":"愿景","暴雨":"豪雨","雷阵雨":"西北雨","滑坡":"山崩","戈壁":"砾漠","地震":"地动","大陆架":"大陆棚","冲积平原":"泛滥平原","冰川":"冰河","地下河":"伏流","泥石流":"土石流","蒸腾作用":"蒸散作用","全球变暖":"全球暖化","厄尔尼诺现象":"圣婴现象","拉尼娜现象":"反圣婴现象","可持续发展":"永续发展","环境保护":"环境保育","橙子":"柳丁","青菜":"清江菜","菠萝":"凤梨","猕猴桃":"奇异果","番石榴":"芭乐","章鱼":"花枝","金枪鱼":"鲔鱼","三文鱼":"鲑鱼","酸奶":"优格乳","酸奶":"优格","方便面":"快餐面","方便面":"速食面","河粉":"粿条","西兰花":"花椰菜","薯片":"洋芋片","空心菜":"通菜","巨无霸":"大麦克","圣代":"新地","奶酪":"起司","甜菜":"红头菜","扎啤":"生啤酒","夜宵":"宵夜","色拉油":"沙拉油","绿色食品":"健康食品","马铃薯":"番薯","便捷酒店":"摩铁","洗手间":"化妆室","少年管教所":"辅育院","小卖部":"福利社","机场":"航空站","停车位":"停车格","发展中国家":"开发中国家","知识产权":"智慧产权","司法部":"法务部","铁路局":"铁工局","二手房":"中古屋","房税":"屋税","地方税务局":"税捐处","国事访问":"国是访问","情报机构":"情治单位","上诉":"抗诉","合约":"契约","合同":"契约","工程":"专案","专案组":"特侦组","声明":"宣告","公交车":"公车","大巴":"游览车","自行车":"脚踏车","地铁":"捷运","摩托车":"机车","的士":"计程车","立交桥":"交流道","旅游":"观光","末班车":"尾班车","航天":"航太","太空船":"太空梭","二手车":"中古车","后视镜":"后照镜","兄弟院校":"姊妹校","托管班":"安亲班","幼儿园":"幼稚园","小学":"国小","初中":"国中","本科":"大学部","研究生院":"研究所","高考":"联考","班主任":"班导","班长":"班代","纪律委员":"风纪股长","文艺委员":"康乐股长","留学":"游学","百分比":"几趴","概率":"机率","变量":"变数","语法":"文法","语意":"意涵","语境":"脉络","普通话":"国语","闽南语":"台语","美式英语":"美语","多选题":"复选题","向量图":"矢量图","最小公倍":"最低公倍","递推":"递回","正态分布":"常态分配","宏观经济学":"总量经济学","微观经济学":"个体经济学","受众":"客群","运营":"营运","渠道":"通路","繁体":"正体","语文":"国文","武术":"国术","京剧":"国剧","民乐":"国乐","受众":"阅听人","宣传":"文宣","北京时间":"中原标准时间","办公室":"事务室","超声波":"超音波","教导处":"训导处","教导主任":"训导主任","屏幕":"荧幕","单反":"单眼","宽带":"宽频","硬盘":"硬碟","硬件":"硬体","鼠标":"滑鼠","数码":"数位","台式电脑":"桌上型电脑","笔记本电脑":"笔记型电脑","智能手机":"智慧手机","移动设备":"行动设备","移动电话":"行动电话","优盘":"随身碟","U盘":"随身碟","内存":"记忆体","空调":"冷气机","打印机":"印表机","调制解调器":"数据机","电子计算器":"电子计数机","打印":"列印","复印":"影印","网络":"网路","博客":"部落格","邮箱":"信箱","短信":"简讯","视频":"视讯","软件":"软体","程序":"程式","上传":"上载","死机":"当机","窗口":"视窗","默认":"预设","设置":"设定","图标":"图示","后缀":"字尾","光标":"游标","模拟":"类比","查看":"检视","点击":"点选","文件夹":"档案夹","互联网":"网际网路","快捷方式":"捷径","打游戏":"打电动","门户网站":"入口网站","登录":"登入","注销":"登出","播放器":"播放软体","比特":"位元","IP地址":"IP位址","C盘":"C糟","D盘":"D糟","人工智能":"人工智慧","士兵":"阿兵哥","解放军":"革命军","原子弹":"核子弹","导弹":"飞弹","核武器":"核子武器","新西兰":"纽西兰","新泽西":"纽泽西","柬埔寨":"高棉","老挝":"寮国","新加坡":"星加坡","朝鲜":"北韩","沙特":"沙乌地","迪拜":"杜拜","蒙古国":"外蒙","意大利":"义大利","悉尼":"雪梨","戛纳":"坎城","卡塔尔":"卡达","突尼斯":"突尼西亚","尼日利亚":"奈及利亚","马尔代夫":"马尔蒂夫","莫桑比克":"莫三鼻给","科特迪瓦":"象牙海岸","塞拉利昂共和国":"狮子山共和国","毛里求斯":"模里细斯","佛罗伦萨":"翡冷翠","赞比亚":"尚比亚","硅谷":"矽谷","澳大利亚":"澳洲","巴布亚新几内亚":"巴巴新几内亚","华盛顿":"华府","马六甲海峡":"麻六甲海峡","肯尼亚":"肯亚","评委":"评审","搭档":"拍档","模特儿":"麻豆","首席执行官":"执行长","首席运营官":"运营长","首席财务官":"财务长","伊斯兰教":"回教","外籍员工":"外劳","工作人员":"从业人员","工人":"劳工","志愿者":"志工","战友":"同袍","儿童":"童子","保安":"保全","黑客":"骇客","户主":"户长","邮递员":"邮差","尼姑":"比丘尼","梵高":"梵谷","毕加索":"毕卡索","里根":"雷根","尼克松":"尼克森","撒切尔":"畲契尔","布什":"布希","奥巴马":"欧巴马","希拉里":"希拉蕊","克林顿":"柯林顿","安吉丽娜茱莉":"安吉丽娜裘莉","普京":"蒲亭","大众汽车":"福斯汽车","奔驰":"宾士","宝马":"BMW","飘柔":"飞柔","强生":"娇生","海飞丝":"海伦仙度斯","索尼":"新力","爱立信":"易立信","阿迪达斯":"爱迪达","加勒比海盗":"神鬼奇航","蜘蛛侠":"蜘蛛人","无间道":"神鬼无间","谍影重重":"神鬼认证","虎胆龙威":"终极警探","这个杀手不太冷":"终极追辑令","憨豆先生":"豆豆先生","铁臂阿童木":"原子小金刚","想干什么":"你想怎样"};var toSimplified={"圜":"圆","溼":"湿","鋂":"镅","甯":"宁","妳":"你","喦":"岩","襬":"摆","滷":"卤","儘":"尽","噹":"当","彙":"汇","滙":"汇","檯":"台","鞦":"秋","鐘":"钟","曏":"向","糰":"团","罎":"坛","颳":"刮","閤":"合","鬍":"胡","迴":"回","穫":"获","纔":"才","纏":"缠","鹸":"硷","髒":"脏","藉":"借","衝":"冲","齣":"出","鼕":"冬","復":"复","傢":"家","捲":"卷","剋":"克","瞭":"了","矇":"蒙","濛":"蒙","懞":"蒙","衊":"蔑","闢":"辟","僕":"仆","韆":"千","繫":"系","鏇":"旋","祗":"只","衹":"只","硃":"朱","埰":"采"};return function(parameter){var options={type:"simplified",str:"",language:""};for(var p in parameter){options[p]=parameter[p]}var source,target,result="",hash={};if(options["type"]=="traditional"){source=simplified_chinese;target=traditional_chinese;for(var i in words){options["str"]=options["str"].replace(i,words[i])}if(options["language"]=="zh_TW"){for(var i in zh_TW){if(options["str"].indexOf(i)>-1){options["str"]=options["str"].replace(new RegExp(i,"g"),zh_TW[i])}}}}else{source=traditional_chinese;target=simplified_chinese;for(var i in words){if(options["str"].indexOf(words[i])>-1){options["str"]=options["str"].replace(new RegExp(words[i],"g"),i)}}for(i in toSimplified){if(options["str"].indexOf(i)>-1){options["str"]=options["str"].replace(new RegExp(i,"g"),toSimplified[i])}}}for(var i=0,len=options["str"].length;i<len;i++){var noReplace=false;var c=options["str"][i];for(var j=0;j<exception.length;j++){var index=options["str"].indexOf(exception[j]);if(i>=index&&i<index+exception[j].length-1){c=exception[j];noReplace=true;break}}if(!noReplace){if(hash[c]){c=hash[c]}else{var index=source.indexOf(c);if(index>-1){c=hash[c]=target[index]}}}result+=c;i+=c.length-1}if(options["type"]=="simplified"){if(options["language"]=="zh_TW"){for(var i in zh_TW){if(result.indexOf(zh_TW[i])>-1){result=result.replace(new RegExp(zh_TW[i],"g"),i)}}}}return result}});</script>\n'
    # Searching
    outputFile = outputFile + '<script type="text/javascript" language="JavaScript">function onSearch(){searchContent = document.getElementById("mySearch").value;var searchContentSC = transverter({type:"simplified",str:searchContent}).trim();var searchContentTC = transverter({type:"traditional",str:searchContent}).trim();var storeId = document.getElementById(\'allFileTable\');var rowsLength = storeId.rows.length;for(var i=1;i<rowsLength;i++){var searchText = storeId.rows[i].cells[0].innerHTML;if(searchText.match(searchContentTC) || searchText.match(searchContentSC) ||  searchText.toUpperCase().match(searchContent.toUpperCase())){storeId.rows[i].style.display=\'\';}else{storeId.rows[i].style.display=\'none\';}}}function doClickFolder(){var searchValue = event.target.innerHTML;searchValue = searchValue.split("\\\\").slice(-1);document.getElementById("mySearch").value = searchValue;onSearch();}function frontpage(){document.getElementById("mySearch").value = "";var storeId = document.getElementById(\'allFileTable\');var rowsLength = storeId.rows.length;for(var i=1;i<rowsLength;i++){storeId.rows[i].style.display=\'\';}}</script>\n'
    outputFile = outputFile + '</head><body><div>\n<table id="allFileTable">'
    if showFirstLine:
        if showFileSize and showFolderAndFile:
            outputFile = outputFile + '<tr><td><span id="fileNameID"></span><input type="text" id="mySearch" ' + howToReactSearch + '="onSearch()" placeholder="搜索..."></td><td>Size</td></tr>'
        if (not showFileSize) or (not showFolderAndFile):
            outputFile = outputFile + '<tr><td>File name:<input type="text" id="mySearch" ' + howToReactSearch + '="onSearch()" placeholder="搜索..."></td></tr>'
    fileCount = 0
    fileSizeCount = 0
    folderCount = 0

    mypath = Path('.')
    for file in mypath.glob('**/*'):
        if showPath:
            loc = file.parent.joinpath(file.name)
        else:
            loc = Path.cwd().joinpath(file)
            print(loc)
        if showProcessDetails:
            print(loc)
        if showAllAddress:
            showName = str(loc)
            showAddr = str(loc)
        else:
            showName = str(file.name)
            showAddr = str(loc)
        if Path.is_dir(file):
            folderCount = folderCount + 1
            showName = '<span class="folder">' + showName + '</span>'
        if Path.is_file(file):
            fileCount = fileCount + 1
        if showFolderAndFile and showFileSize:
            fileSize = Path(loc).stat().st_size
            showFileSize = formatFileSize(fileSize)
            fileSizeCount = fileSizeCount + fileSize
            if clickFolder and Path.is_dir(file):
                outputFile = outputFile + '<tr><td><a onclick="doClickFolder()" href="javascript:void(0);">' + showName + '</td><td>' + showFileSize + '</a></tr>\n'
            else:
                outputFile = outputFile + '<tr><td><a href="' + showAddr + '">' + showName + '</td><td>' + showFileSize + '</a></tr>\n'
        if (not showFolderAndFile and Path.is_dir(file)) or (not showFileSize):
            if clickFolder:
                outputFile = outputFile + '<tr><td><a onclick="doClickFolder()" href="javascript:void(0);">' + showName + '</a></td></tr>\n'
            else:
                outputFile = outputFile + '<tr><td><a href="' + showAddr + '">' + showName + '</a></td></tr>\n'
   
    outputFile = outputFile + '</td></table></div></body></html>'
    outputFile = outputFile + '<script type="text/javascript" language="JavaScript">document.getElementById("fileNameID").innerHTML = "<a href=\\"javascript:frontpage()\\">Name</a> (' + str(fileCount) + ' files in ' + str(folderCount) + ' folders'
    if showFileSize:
        outputFile = outputFile + ', '+ formatFileSize(fileSizeCount)
    outputFile = outputFile +  ') ";</script>'
    writefile(outputFile)
    
if __name__ == '__main__':
    main()