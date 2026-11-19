---
url: https://arxiv.org/pdf/2403.08501
fetched: 2026-11-18
publisher: "arXiv (Centre for the Governance of AI)"
published: 2024-03-13
original: 2026-11-18 Heim et al 2024 Governing Through the Cloud.pdf
license: "CC BY 4.0"
rehost: yes
---

_Markdown copy of 2026-11-18 Heim et al 2024 Governing Through the Cloud.pdf, made 2026-11-18. The original is the authority._
WHITEPAPER
March 2024
GOVERNING THROUGH THE CLOUD: THE INTERMEDIARY ROLE OF
COMPUTE PROVIDERS IN AI REGULATION
Lennart Heim, Tim Fist, Janet Egan, Sihao Huang, Stephen Zekany, Robert Trager, Michael A. Osborne
& Noa Zilberman
In partnership with
4202
raM
62
]YC.sc[
2v10580.3042:viXra

Governing Through the Cloud:
The Intermediary Role of Compute Providers in AI
Regulation
LennartHeim,∗†1 TimFist,∗2 JanetEgan,∗3 SihaoHuang,∗4
StephenZekany,∗‡1 RobertTrager,∗1,6,7 MichaelAOsborne,5,7 NoaZilberman5
1CentrefortheGovernanceofAI(GovAI),2CenterforaNewAmericanSecurity,InstituteforProgress,
3HarvardKennedySchool,4DepartmentofPoliticsandInternationalRelations,UniversityofOxford,
5DepartmentofEngineeringSciences,UniversityofOxford,6BlavatnikSchoolofGovernment,Universityof
Oxford,7OxfordMartinAIGovernanceInitiative
Abstract
Asjurisdictionsaroundtheworldtaketheirfirststepstowardregulatingthemost
powerfulAIsystems,suchastheEUAIActandtheUSExecutiveOrder14110,
there is a growing need for effective enforcement mechanisms that can verify
complianceandrespondtoviolations. Wearguethatcomputeprovidersshould
havelegalobligationsandethicalresponsibilitiesassociatedwithAIdevelopment
anddeployment,bothtoprovidesecureinfrastructureandtoserveasintermediaries
forAIregulation. Computeproviderscanplayanessentialroleinaregulatory
ecosystem via four key capacities: as securers, safeguarding AI systems and
criticalinfrastructure; asrecordkeepers, enhancingvisibilityforpolicymakers;
as verifiers of customer activities, ensuring oversight; and as enforcers, taking
actionsagainstruleviolations. Weanalyzethetechnicalfeasibilityofperforming
thesefunctionsinatargetedandprivacy-consciousmannerandpresentarangeof
technicalinstruments. Inparticular,wedescribehownon-confidentialinformation,
to which compute providers largely already have access, can provide two key
governance-relevantpropertiesofacomputationalworkload: itstype—e.g.,large-
scaletrainingorinference—andtheamountofcomputeithasconsumed. Using
AIExecutiveOrder14110asacasestudy,weoutlinehowtheUSisbeginningto
implementrecordkeepingrequirementsforcomputeproviders. Wealsoexplore
howverificationandenforcementrolescouldbeaddedtoestablishacomprehensive
AI compute oversight scheme. We argue that internationalization will be key
to effective implementation, and highlight the critical challenge of balancing
confidentialityandprivacywithriskmitigationastheroleofcomputeprovidersin
AIregulationexpands.
Each author contributed ideas and/or writing to the paper. However, being an author does not imply
agreementwitheveryclaimmadeinthepaper.
∗Denotesprimaryauthorswhocontributedmostsignificantlytothedirectionandcontentofthepaper.Both
primaryauthorsandotherauthorsarelistedinapproximatelydescendingorderofcontribution.
†Correspondencetolennart.heim@governance.ai.
‡WorkcompletedwhilstaSummerResearchFellowattheCentrefortheGovernanceofAI,Oxford.

ExecutiveSummary
Introduction—JurisdictionsaroundtheworldaretakingtheirfirststepstowardregulatingAI,such
astheEUAIActandtheUSExecutiveOrder14110. Whiletheseregulatoryeffortsmarksignificant
progress,theylackrobustmechanismstoverifycomplianceandrespondtoviolations. Wepropose
computeserviceproviders(computeprovidersbelow)asanimportantnodeforAIsafety,bothin
providingsecureinfrastructureandactinginanintermediaryroleforAIregulation,leveragingtheir
unique relationships with AI developers and deployers. Our proposal is not intended to replace
existingregulationsonAIdevelopersbutrathertocomplementthem. (Section1)
ComputeProviders’IntermediaryRole—Increasinglylargeamountsofcomputingpowerarenec-
essaryforboththedevelopmentanddeploymentofthemostsophisticatedAIsystems. Consequently,
advancedAImodelstodayaretrained,anddeployedindatacenters,housingtensofthousandsof
“AIaccelerators”(specializedcomputersforAIapplications). Becauseofthelargeupfrontcostof
buildingthisinfrastructureandeconomiesofscale,AIdevelopersoftenaccesslarge-scalecompute
through models like Infrastructure as a Service (IaaS), also often described as cloud computing.
(Section1.1)
Implements & Sets
helps enforce Regulations
AAII regulations CCoommppuuttee & Oversight
CCoommppaanniieess PPrroovviiddeerrss RReegguullaattoorrss
Subject to
““TTaarrggeett”” ““IInntteerrmmeeddiiaarryy”” Reports
Compliance
Violations
Checks
Figure1: TheintermediaryroleofcomputeprovidersinrelationtoAIcompaniesandregulators.
SomeleadingAIfirmscurrentlymanagetheirowndatacentersormaintainexclusivepartnerships
withleadingentitiesinthisdomain,knownashyperscalers. Notably,themostadvancedAIresearch
is currently being conducted at or with these hyperscalers (e.g., Microsoft Azure, Amazon Web
Services(AWS),Apple,Bytedance,Meta,Oracle,Tencent,andGoogleCloud). Whilethissituation
presentscomplexchallengesforregulatoryoversight,ourdiscussionalsoencompassesscenariosin
whichcomputeprovidersareinternaltoorcloselylinkedwithanAIfirm.
WefocusonfrontierAIsystems,whichhavethepotentialtogiverisetodangerouscapabilitiesand
poseseriousrisks. Asthesesystemsnecessitateextensiveamountsofcomputetotrainanddeployat
largescales,targetingcomputeprovidersbecomesapromisingmethodtooverseethedevelopment
anddeploymentofsuchsystems. Furthermore,thistargetnarrowstheregulatoryscopetothesmaller
setofkeycustomerswhoarebuildingAIsystemsatthefrontier,therebyminimizingtheburdens
associatedwithregulatorycomplianceandenforcement. (Section1.2)
GovernanceCapacities—Weproposethatcomputeproviderscanleveragetheircrucialroleinthe
AIsupplychaintosecureinfrastructureandserveastheintermediatenodeinsupportofregulatory
objectiveswhilemaintainingcustomers’privacyandrights.TheycanfacilitateeffectiveAIregulation
viafourkeycapacities: assecurers,recordkeepers,verifiers,and,insomecases,evenenforcers.
Reportingrepresentsarelatedyetdistinctdimension,whereincomputeprovidersprovideinformation
toauthoritiesasmandatedbylaworregulations. (Section2)
3

|          | Governance    | Capacities   |             |
| -------- | ------------- | ------------ | ----------- |
| Security | RecordKeeping | Verification | Enforcement |
Helpingprovidephysical Theselectivecollection, Activelyverifyingcustomer Restrictionorlimitationof
andcybersecuritymeasures organization,and identities,specificactivities, computeaccessto
tosecuretheAImodel, maintenanceofhigh-level andhigh-levelAIsystems’ customersorworkloadsfor
relatedintellectual informationofacompute properties. non-compliantcustomers.
| property,andpersonaland | provider’sinfrastructure |     |     |
| ----------------------- | ------------------------ | --- | --- |
| confidentialdata.       | usage,suchasacustomer’s  |     |     |
computeusagedata.1
Enables
Enablessharedsecurity IncreasesvisibilityintoAI Ensuresthatthe Directlyimpactsthe
standardstoprotectthe development,links deploymentand capabilityofcustomersto
publicgood,suchas customersandtheirusage developmentofAIsystems developordeploy
safeguardingcritical toreal-worldactors,and adheretoregulationsor advancedAIsystems,
infrastructureandhelping enablespost-incident companypoliciesand ensuringadherenceto
preventmodeltheft. attributionsandforensics. reportedproperties. rules.
Examples
HelppreventIP(e.g., Obtaininsightsinto Confirmcompliancewith Restrictaccessto
algorithms),modelweights, nationalcomputeuse mandatoryreportingover customerslackinglicenses
andtrainingdatafrom trendsforpolicy trainingcompute asanAIdeveloperfortheir
beingstolenbymalicious formulation,suchas thresholds. system.
| actors.              | computedistribution(e.g., |                        |                  |
| -------------------- | ------------------------- | ---------------------- | ---------------- |
|                      | USNAIRR).                 | Verifycompliancewith   | Refusetodeployan |
| Helppreventattackson |                           | datausageguidelinesfor | unlicensedor     |
large-scaledeploymentsof Enablemonitoringfor frontierAItraining. non-compliantAImodel.
| foundationalmodelsthat | suspectedviolationsofthe |     |     |
| ---------------------- | ------------------------ | --- | --- |
couldshutdowndozensof reportingrequirements Verifyifthedeployed DisableAIsystemsthat
criticalservices underExecutiveOrder frontierAIsystemhasan demonstrateactivitythatis
nationwide. 14110. adequatelicenseor undesirable,uncontrollable,
|     |                         | certification. | orinviolationof           |
| --- | ----------------------- | -------------- | ------------------------- |
|     | Collectinformationonthe |                | regulations(e.g.,computer |
|     | environmentalimpactofAI |                | worm-likeAIsystem).       |
computeuse.
Table1: Summaryofthekeygovernancecapacitiesthatcomputeproviderscanenable.
TechnicalFeasibility—Ouranalysisindicatesthesegovernancecapabilitiesarelikelytobetech-
nicallyfeasibleandpossibletoimplementinaconfidentiality-andprivacy-preservingwayusing
techniques available to compute providers today. Compute providers often collect a wide range
ofdataontheircustomersandworkloads,forthepurposesofbilling,marketing,serviceanalysis,
optimization,andfulfillinglegalobligations. Muchofthisdatacouldalsobeusedtosupportidentity
verification,aswellasverifyingtechnicalpropertiesofworkloads. Ataminimum,providershave
accesstobillinginformationandcanaccessbasictechnicaldataonhowtheirhardwareisused. This
likelymakesitpossibleforcomputeproviderstodeveloptechniquestodetectandclassifycertain
relevantworkloads(e.g.,whetheraworkloadinvolvestrainingafrontiermodel)andtoquantifythe
amountofcomputeconsumedbyaworkload. Verificationofmoredetailedpropertiesofaworkload,
suchasthetypeoftrainingdataused,orwhetheraparticularmodelevaluationwasrun,couldbe
usefulforgovernancepurposesbutisnotcurrentlypossiblewithoutdirectaccesstocustomercode
anddata. Withfurtherresearchanddevelopmentefforts,computeprovidersmaybeabletooffer
“confidentialcomputing”servicestoallowcustomerstoprovethesemoredetailedpropertieswithout
| otherwiserevealingsensitivedata. | (Section3) |     |     |
| -------------------------------- | ---------- | --- | --- |
1Focusingonessentialdatathatinformswithoutcompromisingprivacyandconfidentiality.
4

ConstructinganOversightScheme—ViaExecutiveOrder14110theUSgovernmentisalready
beginningtoimplementrecordkeepingrolesforcomputeprovidersbyrequiringthemtoimplement
aCustomerIdentificationProgram(essentiallyaKnow-Your-Customer(KYC)program)forforeign
customers,andtoreportforeigncustomertrainingofhighlycapablemodelstogovernment. Expand-
ingtheroleofcomputeproviderstoalsorecordandvalidatedomesticcustomersusingcomputeat
frontierAIthresholdscouldenabletheUSgovernmenttoidentifyandaddressAIsafetyrisksarising
domestically. Complementingthesemeasureswithverificationandenforcementrolesforcompute
providerscouldfurtherenabletheconstructionofacomprehensivecomputeoversightscheme,and
| ensurethatAIfirmsanddevelopersarecomplyingwithAIregulations. |     |     |     | (Section4) |     |
| ------------------------------------------------------------ | --- | --- | --- | ---------- | --- |
U.S. Department of Commerce
|     | Bureau of Industry  |     | National Institute of Standards  |     |     |
| --- | ------------------- | --- | -------------------------------- | --- | --- |
|     | and Security (BIS)  |     | and Technology (NIST)            |     |     |
Compute
| Report              |             | Report         |     |                          | Sets safeguards  |
| ------------------- | ----------- | -------------- | --- | ------------------------ | ---------------- |
|                     | provider    |                |     | Report large AI models,  |                  |
| large clusters and  | supervision | violations of  |     | security measures, and   | and regulations  |
| foreign companies   |             | regulations    |     | evaluation results       |                  |
Reporting
|     | Compute  |     |              | Domestic AI  |     |
| --- | -------- | --- | ------------ | ------------ | --- |
|     | Provider |     | Verification | Developer    |     |
Assist
enforcement
| Report large training  | Enforce relevant  |     |     |     |     |
| ---------------------- | ----------------- | --- | --- | --- | --- |
controls
runs, IP addresses, etc.
Key
Current proposed regulation
|     | Foreign Customers |     |     | Proposed additions |     |
| --- | ----------------- | --- | --- | ------------------ | --- |
Figure2: Additionalmeasures,implementedbytheDepartmentofCommerce,wouldstrengthenthe
intermediaryroleofcomputeprovidersandenableacomputeoversightscheme.
TechnicalandGovernanceChallenges—Torealizearobustgovernancemodel,severaltechnical
andgovernancechallengesremain. TheseincludeidentifyingadditionalmeasurablepropertiesofAI
developmentthatcorrespondtopotentialthreats,makingworkloadclassificationmethodsrobustto
potentialevasion,andformulatingprivacy-preservingverificationprotocols. (Section5.1)
The success of our proposed oversight scheme hinges on its multilateral adoption to prevent the
migrationofAIactivitiestojurisdictionswithlessstringentoversight. Foraninternationalframework
tobedurableandeffective,itmustaddressconcernsfromnon-USgovernments. Cooperationwill
needtoaccountforcomplexprivacyandoversightissuesassociatedwithgloballyspreaddatacenters.
ComputeprovideroversightmayaffectcompetitionintheAIecosystemandraiseconcernsabout
issuesofnationalcompetitiveness,and,consequently,thismayinfluencetheabilityofUSprovidersto
offerproductsglobally,includingtoforeignpublic-sectorcustomers. Industry-ledprivacy-preserving
standardscouldhelpensuretrust,butfurtherresearchisneededtoincentivizebroadinternational
| buy-intoaglobalframework. |     | (Section1.4andSection5.2) |     |     |     |
| ------------------------- | --- | ------------------------- | --- | --- | --- |
Conclusion—Computeprovidersarewell-placedtosupportexistingandfutureAIgovernance
frameworksinaprivacy-preservingmanner. Manyoftheinterventionsweproposearefeasiblewith
thecurrentcapabilitiesofcomputeproviders. However,realizingthefullpotentialnecessitatesad-
dressingtechnicalandgovernancechallenges,requiringconcertedeffortsinresearchandinternational
cooperation. AsgovernmentsandregulatorybodiesmovetoaddressAIrisks,computeproviders
standastheintermediatenodeinensuringtheeffectiveimplementationofregulation. (Section6)
5

Contents
ExecutiveSummary 3
1 Introduction 7
1.1 ComputeProviders’IntermediaryRole . . . . . . . . . . . . . . . . . . . . . . . . 7
1.1.1 RegulatoryIntermediaries . . . . . . . . . . . . . . . . . . . . . . . . . . 8
1.2 FocusonFrontierAI . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9
1.3 OverviewofourContributions . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9
1.4 LimitationsandFutureResearchDirections . . . . . . . . . . . . . . . . . . . . . 10
2 GovernanceCapacitiesofComputeProviders 10
2.1 ComputeProvidersintheAIComputeSupplyChain . . . . . . . . . . . . . . . . . 11
2.2 GovernanceCapacities . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12
2.2.1 I.Security . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12
2.2.2 II.RecordKeeping . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14
2.2.3 III.Verification . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16
2.2.4 IV.Enforcement . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17
3 TechnicalFeasibilityofComputeProviders’GovernanceRole 18
3.1 Security . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20
3.2 RecordKeeping . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20
3.3 Verifying . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21
3.3.1 IdentityVerification . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21
3.3.2 WorkloadClassification . . . . . . . . . . . . . . . . . . . . . . . . . . . 23
3.3.3 ComputeAccounting . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26
3.3.4 DetailedWorkloadVerification. . . . . . . . . . . . . . . . . . . . . . . . 29
4 ConstructinganOversightScheme 30
4.1 CaseStudy: ComputeProviders’IntermediaryRoleintheUS . . . . . . . . . . . . 31
4.1.1 RecordKeepingandReportingintheAIExecutiveOrder . . . . . . . . . . 31
4.1.2 PotentialforVerificationCapacity . . . . . . . . . . . . . . . . . . . . . . 32
4.1.3 FutureAdditions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 32
4.2 RegulatingtheComputeProvidersThemselves . . . . . . . . . . . . . . . . . . . 34
4.3 DomesticGovernmentCapacity . . . . . . . . . . . . . . . . . . . . . . . . . . . 34
4.4 InternationalCoordination . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 35
5 KeyChallenges 37
5.1 TechnicalChallenges . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 37
5.2 GovernanceChallenges . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 39
6 Conclusion 40
A OverviewofComputeProviderTechnologies 41
B ObservableDataAttributes 42
References 46
6

1 Introduction
Asgovernments,internationalorganizations,andregionalbodiesformulateapproachesforgoverning
advancedAI,weask: howcanauthoritiesgainvisibilityintodevelopmentanddeploymentpractices
andenforcerules? ThevisibilityiscurrentlyobscuredbecausefrontierAIdevelopmentlargelytakes
placewithintheprivatesectorandoftenreliesonself-reportingbyAIcompanies,whichmaynot
alwaysbereliableduetogrowingincentivestoobfuscatetheresults(Anderljungetal.,2023b;Mulani
& Whittlestone, 2023; Whittlestone & Clark, 2021). Ongoing governance processes worldwide
requireanswerstothisquestion.
JurisdictionsincludingChina,theEuropeanUnion(EU),theUnitedKingdom(UK),andtheUnited
States(US)areattemptingtoimposenewreportingrequirementsonAIfirmsandcomputeproviders
(FutureofLifeInstitute,2024;Jiang&Cao,2023;SecretaryofStateforScience,Innovationand
Technology,2023;SenatorScottWiener,2024;Sheehan,2024;TheWhiteHouse,2023b). They
arealsobeginningtoregulatethedevelopmentanddeploymentofmodelswithpotentiallyharmful
capabilities. Yet,enforcingtheserulesproveschallenging;withoutappropriatemechanisms,itis
difficulttodetectviolations(Hacker,2023;Whittlestoneetal.,2023). Governanceapproaches,such
astherecentUSExecutiveOrder(TheWhiteHouse,2023b)andtheEU’sproposedAIAct(Council
oftheEuropeanUnion,2024), havenotdevelopedpracticalmeanssuchasrobustspot-checking
(randomizedinspectionstoensurecompliance)andevidence-gatheringmechanismsforachieving
thesegoals.
Thispaperdemonstrateshowcomputeproviders—firmswhomakecomputingresources(“compute”
below)2 availableforAIdevelopmentanddeployment—caneffectivelyserveasanintermediaryfor
frontierAIgovernancebetweengovernmentsandthefirmsdevelopinganddeployingAI.Inthisrole,
computeproviderscanactasafirstlineofdetectionofviolationsofagovernanceregimeandeven
defendagainstviolations.
1.1 ComputeProviders’IntermediaryRole
Large amounts of computing power are necessary for both the development and deployment of
frontierAIsystems. Consequently,advancedAImodelsaretrained,anddeployed,indatacenters3,
housing tens of thousands of AI accelerators. Because of the large upfront cost of building this
infrastructure,AIdevelopersoftenaccesslarge-scalecomputethroughmodelslikeIaaS4,alsooften
describedascloudcomputing.5 Throughoutthispaper,werefertoentitiesthatprovideaccesstothis
computationalpowerascomputeproviders.
Some AI firms currently manage their own data centers or maintain exclusive partnerships with
leading compute providers, known as hyperscalers.6 Notably, the most advanced AI research is
currentlybeingconductedatorwiththesehyperscalers.7 Whilethissituationintroducescomplex
challengesforregulatoryoversight,ourdiscussionalsoencompassesscenariosinwhichcompute
2Foradiscussionofcomputeasagovernancenode,seeSastryetal.(2024).
3Our focus is on the entities that own and operate data centers, prioritizing the “legal entity” level of
abstractionoverthephysicallocationsor“datacenters”themselves.
4This discussion extends to services that offer hardware access with sufficient flexibility for customer-
definedusage,whichmayoccasionallyencompasscertainPlatform-as-a-Service(PaaS)offerings.However,
ouremphasisisonscenariosinwhichusagesurpassescertainAIcomputethresholdsthatareofrelevancefor
frontierAI.Incontrast,servicesprovidingaccesstopre-configuredAImodels(Software-as-a-Service,orSaaS)
falloutsideourdefinedscopeofcomputeproviders.(Thesuggestedgovernancecapacitiescouldstillhelpifthe
regulationoftheseservicesisdesired.)
5Theterm“cloud”ismoreassociatedwithaspecificbusinessmodelratherthantheunderlyingactivityof
providingcomputeresources.Forthiscontext,weprefertheterm“computeproviders”toaccuratelyreflectthe
focusontheprovisionofcomputingpower.Thischoicealsoallowsustoincludeentitiesthatpredominantly
providetheircomputationalresourcesinternally(e.g.,Meta(Janardhan,2023))withinthescopeofourdiscussion.
6ThemostnotablehyperscalersincludeMicrosoftAzure,AmazonWebServices(AWS),Apple,Bytedance,
Meta,Oracle,Alibaba,Tencent,andGoogleCloud(Vailshery,2024).
7ManyprominentAIcompanieseitheroperateashyperscalersthemselvesormaintainstrategicpartnerships
with them. For example, OpenAI’s collaboration with Microsoft (Microsoft Corporate Blogs, 2023), and
Anthropic’sassociationswithAWSandGoogleCloud(Amazon.com,Inc.,2023b;Anthropic,2023),exemplify
suchrelationships.
7

providersareinternalto,orcloselylinkedwithanAIfirm.8 Forexample,anAIcompanyshould
notbeabletocircumventtheproposedguidelinesbycategorizingitsusageasinternalprovisionsor
failingtoidentifyitselfasacustomer. Thiswouldensurecomprehensivecoverageofallrelevant
formsofcomputeprovisionforfrontierAI.
Implements & Sets
helps enforce Regulations
AAII regulations CCoommppuuttee & Oversight
CCoommppaanniieess PPrroovviiddeerrss RReegguullaattoorrss
Subject to
““TTaarrggeett”” ““IInntteerrmmeeddiiaarryy”” Reports
Compliance
Violations
Checks
Figure1: TheintermediaryroleofcomputeprovidersinrelationtoAIcompaniesandregulators.
1.1.1 RegulatoryIntermediaries
Theuseofprivatesectorentitiesasregulatoryintermediariesisnotanewconcept(Abbottetal.,
2017a;b;Hay&Shleifer,1998). Regulationsfortheaviationindustryrequireairlineoperatorsto
maintainsecurityplans,keeprecordsonpassengers,verifypassengeridentities,anddenyboardingin
responsetospecifiedviolations(ECFR,2024;AviationTransportSecurityAct,2005). Inthecontext
ofcommunicationserviceproviders,somegovernmentshaveenacteddataretentionpoliciesthat
requirethecollectionandretentionofinformationoncustomers’activitiesforaspecifiedamount
oftime(AustralianAttorney-General’sDepartment,2015;CountryLegalFrameworksResource,
2023). Internationallycoordinatedanti-moneylaunderingandcounter-terrorismfinancingstandards
requirefinancialinstitutionstokeeprecords,verifyidentities,andacttopreventillicitflowsofmoney
(FinancialActionTaskForce,2023).
Compute providers are already subject to regulations that dictate operational standards and data
managementpractices. Forexample,lawstargetingChildSexualAbuseMaterial(CSAM)impose
obligationsoncomputeproviderstodetectandreportsuchcontent(Amazon.com,Inc.,2023a;Biden,
2008; European Union, 2011). Data protection regulations, such as the General Data Protection
Regulation (GDPR) in the EU, set stringent requirements for data handling, privacy, and user
consent, which significantly affect how compute providers manage and secure user data (AWS,
2024a;EuropeanUnion,2016;GoogleCloud,2021). Additionally,legislationaimedatcombating
terrorismandextremismmayrequirecomputeproviderstomonitorandrestrictthedisseminationof
harmfulcontent(EuropeanUnion,2021).
8Theserelationshipsandtheconcentratedmarketforlarge-scalecomputehavegivenrisetoantitrustand
competitionconcerns,drawingscrutinyfromregulators,includinganongoinginquirybytheUSFederalTrade
Commission(FederalTradeCommission,2024)andaninvestigationbytheUKCompetitionandMarkets
Authority (Milmo, 2023). While we acknowledge the need to carefully analyze how enhanced regulatory
measuresmayimpactcompetitionissuesinthesector, weexpecttheimpacttobelimitedandnotbroadly
significant.Thisisduetothefocusedscopeofthemeasures,targetingonlythosecomputeproviderscapable
ofsupportinglarge-scaleAIinfrastructureandcustomerswhoarerunninglarge-scaleworkloadscostingtens
tohundredsofmillionsofdollarsormore.Adetaileddiscussionoftheseantitrustconcernsrequiresbroader
analysisandisbeyondthescopeofthispaper.
8

1.2 FocusonFrontierAI
ThecustomerbaseofAIcomputeprovidersisdiverse,rangingfromindividualsandsmallenterprises
tolargecorporationsandgovernmentagencies. However,theprimaryfocusofthispaperisona
subsetofAIsystemsknownasfrontierAI.FrontierAIsystemsaredefinedas“highlycapablegeneral-
purposeAImodelsthatcanperformawidevarietyoftasksandmatchorexceedthecapabilities
presentintoday’smostadvancedmodels”(UKDSIT,2023).9 Thesesystemsrepresentthefrontier
ofcurrentAIcapabilitiesandcurrentlyrequiresubstantialcomputeresourcesfortheirdevelopment
andoperation(Anderljungetal.,2023a;Sastryetal.,2024;Sevillaetal.,2022).
Giventhesignificantcomputeandresearchdemands,onlyasmallnumberofentitiespossessthe
necessaryresourcestodevelopfrontierAIsystems. Thispaperaddressesprimarilylargecorporations
forregulatoryconsideration. Theintentoftheproposedregulatoryframeworksisnottoencompass
theentiretyofcomputeproviders'customerbaseindiscriminately. Rather,thefocusislimitedto
thoseactorswhoareinapositiontodevelopordeployfrontierAIsystems—basedontheircompute
usage—warranting closer scrutiny and potential regulation. This targeted approach ensures that
regulatory measures are both effective and proportional, avoiding unnecessary encumbrances on
smallerentitiesorindividualuserswhodonotfallwithintherelevantfrontierAIactivities.10 Sastry
etal.(2024)discusstheimportanceofcomputeforfrontiermodelsinmoredetailandexaminethe
conditions under which compute, and by extension, compute providers, serve as effective policy
levers,aswellasscenariosandconditionswheretheirimpactislimited.
1.3 OverviewofourContributions
Wesuggestthatcomputeproviderscanplayakeyroleingovernanceregimessimilartotheexamples
listedaboveviafourkeycapacities: assecurers,recordkeepers,verifiers,andenforcers. Security
canrestrictaccesstoAI-relatedIP,suchasthemodelweights, frombadactors. Recordkeeping
allows selected information gathering for insights into AI activities and allows for post-incident
attribution. VerificationincludescheckingcustomeractivitiesandAIsystemstoverifycompliance
withregulationsandstandards. Enforcemententailstherestrictionorlimitationofcomputeaccess
fornon-compliantcustomers.
Weanalyzethetechnicalmeansofperformingeachofthesefunctions. Concerningsecurity, we
outlinetherolemanycomputeprovidersalreadyserveinestablishingbaselinelevelsofphysical,
infrastructure,andnetworksecurity,andbrieflydiscusshowthisroleshouldbeexpandedtoaddress
more sophisticated threats. Regarding record keeping, we describe the information that is likely
alreadyavailabletocomputeprovidersandthepotentialinsightsitcanoffer. Regardingenforcement,
wereviewthecapabilitiesofdatacenterproviderstofacilitatetheenforcementofstandards,eitherof
anexternalgovernanceregimeoroftheirowntermsofservice.
Wefocusmuchofourtechnicalanalysisontherolecomputeproviderscouldplayinverification
inatargetedandprivacy-consciousmanner. Wedescribeinformationthatisalreadyavailableto
computeprovidersthatcanbeusedforfoursub-categoriesofverification: workloadclassification,
computeaccounting,verificationofpropertiesofcodeanddata(“detailedworkloadverification”),
andidentityverification,suchasKnow-Your-Customer(KYC)regimes(Egan&Heim,2023;Smith,
2023). Several of these techniques couldbe used in real-time to establish whethera customer is
engaginginanactivitythatmightbesubjecttoregulatoryoversight. Ifcomputeproviderswereto
implementthesetechniques,theycouldlikelydistinguishwhethertheircustomersareengagingin
activitiessuchastrainingalargemodel,orengagingininferenceatscale,aswellasquantifythe
amountofcomputeconsumedbylargeworkloads
Afterdescribingthetechnicalpossibilities,wefocusontheUS,explaininghowsomeofthetechniques
wedescribecanfacilitatecompliancewiththemandatesoftheBidenAdministration’s2023Executive
Order14110onSafe,Secure,andTrustworthyAI(hereafter“theAIExecutiveOrder”)andsupport
itsoverallobjectives(TheWhiteHouse,2023b).Weidentifyasetofnextstepsforcomputeproviders
toverifythatmodeldevelopershavemettheirSection4requirementsundertheAIExecutiveOrder.
9AlsoseeSection2.1ofAnderljungetal.(2023a).
10InSection5.2,weelaborateonprivacyandconfidentialityconsiderations,emphasizingthatourproposed
regulatorymeasuresarespecificallyaimedatkeyactorsinfrontierAIdevelopment,ratherthanbeingbroadly
appliedtotheentirecustomerbaseofcomputeproviders,suchasindividuals.Heim&Egan(2023)andEgan&
Heim(2023)alsodiscusstheideaof“above-thresholdcomputeusage.”
9

WefurtherarguethatthebroadgoalsoftheAIExecutiveOrdercouldbenefitfromthefullrangeof
techniquesdescribedhere,particularlywheninternationalized. Inthefinalsection,wehighlightthe
technicalandgovernancechallengesandopportunitiesfortechnicalgovernanceandpolicyresearch.
1.4 LimitationsandFutureResearchDirections
Inthispaper,weproposeaconceptualmodelwhereincomputeprovidersimprovetheefficiencyand
effectivenessofthedevelopingregulatoryAIecosystem. Ourdiscussionisnotacomprehensive
policyblueprintreadyforimplementation. Whilecertainaspectsofourproposalmaybedirectly
actionable,otheraspectsrequiremoreevaluation. Ourprimaryobjectiveistoargueforparticular
rolesforcomputeprovidersandtostimulateadebate: Shouldcomputeprovidersembracetheroles
we have outlined? Which of the proposed activities are most viable, and which require further
research?
Whileweemphasizetheneedtointernationalizeourproposedconcept,weacknowledgethatthis
aspect is not explored in detail, especially the legal aspects. The complexity of such an analysis
extendsbeyondthescopeofthispaper,callingfordetailedlegalandpolicyanalysis. Ouraimisto
motivatemoreresearchinthisdomain,recognizingtheneedforamorecomprehensiveinvestigation
intotheintricaciesinvolvedinapplyingtheseregulatoryconceptsacrossdifferentjurisdictions. This
isparticularlyrelevantgiventheintricatechallengesthathaveemergedinthepast,suchasthose
surroundingtheEU-USPrivacyShield,andothers(Buttarelli,2018).
Someofthesuggestedregulatorymeasuresmayhaveimplicationsonprivacyandconfidentiality
forcustomersofcomputeprovidersandwerecognizethatincreasinglegalreportingrequirements
must be carefully weighed against the potential for misuse or government overreach. However,
ourfocus—frontierAI—largelypertainstocompute-intensiveworkloadsundertakenbyalimited
numberofcorporateentities. Thissimplifiestheregulatorylandscapewithrespecttoinformation
describingtheseworkloadsandthecompaniesrunningthem,asstringentprivacyregulationslikethe
GDPRsafeguardthepersonaldataofindividuals(“naturalpersons”),whiletypicallyimposingfewer
constraintsondatarelatedtocompanies(“juridicalperson”).
TheurgencyofthisdiscourseismagnifiedbytheKYCrequirementsoutlinedintheUS’sAIExecu-
tiveOrder,withimplementationcurrentlybeingprogressedthroughtheDepartmentofCommerce’s
proposed rule (Federal Register, 2024).11 Reaching a comprehensive and thoughtful regulatory
frameworkrequiresgoingbeyondunilateralmeasures,whichcouldleadtounintendedadverseconse-
quences. Internationalcoordinationiscrucialtoaddressthequestionsarisingfromtheintersectionof
AIregulationwithinternationaltradelaw,confidentiality,andprivacy. Thispapercontributestothe
dialogueandadvocatesforanAIregulatoryframeworkthatiscollaborative,nuanced,effective,and
globallyinclusiveandresponsive.
2 GovernanceCapacitiesofComputeProviders
Inthecurrentecosystem,frontierAImodelsaretrainedanddeployedusinglargecomputeclusters
consistingofthousandstotensofthousandsofAIaccelerators(Pilz&Heim,2023;Sevillaetal.,
2022).Theconcentratedsupplychain,inadditiontothedetectability,excludability,andquantifiability
ofphysicalcomputinghardware,makescomputeaparticularlyeffectivenodeofgovernancecompared
tootherinputstoAIdevelopment(Belfield&Hua,2022;Pilz&Heim,2023).
Therefore,thephysicalinfrastructurerequiredforAIdevelopmentanddeploymentcanbeusedas
aninstrumenttoenhanceexistingAIregulations—makingthemmoreefficientandeffectivewhile
enablingnewpolicies. Computeproviderscanperformthesefunctionsviafourkeycapacities: as
securers,toprotectIP;recordkeepers,enablingdatacollectionforanalysisandfuturereference;
asverifiersofcustomeractivities,enablingappropriateoversight;andasenforcers,takingactions
againstnormandruleviolations. Wediscussthesecapacitiesinthissectioninmoredetail.
Thisapproachoffersanuancedalternativetobroadmeasuressuchaschipexportcontrols(Allen,
2022),positioningcomputeprovidersasamorepreciseandadaptablegovernancemechanismwithin
11Especially,assomeofthecurrentlyproposedmeasuresmaybeoverlybroad,potentiallyviolatingconfiden-
tialityprinciples.
10

theAIsupplychain.Unlikecontrolsonphysicalcomputinghardware,thedynamicmodelofcompute
provisionaffordsahigherdegreeofflexibilityandspecificity(Table1inHeim&Egan(2023)).
|     | 2.1 ComputeProvidersintheAIComputeSupplyChain |     |     |     |     |     |
| --- | --------------------------------------------- | --- | --- | --- | --- | --- |
IntheAIsupplychain,computeprovidersactasanintermediary,offeringcomputationalresources
tocustomers. Theseprovidershouselargenumbersofchipsintheirdatacenterfacilities,operating
themcost-effectivelyinlargequantitieswithnecessaryelementssuchaspower,land,cooling,and
connectivity,andoptimizingthemfordevelopinganddeployingAImodels(Figure3). Withcurrent
technologies,traininglargeAIsystemsrequiresphysicallyco-locatedchips. Thishascausedmuch
ofcontemporaryAIdeploymentanddevelopmenttooccurinlargefacilities,whereincomputeis
madeavailabletocustomersdigitallyandremotely,oftenthroughmodelslikeInfrastructureasa
Service(IaaS)orcloudcomputing. Thecomputeproviderindustryhasseensignificantconsolidation
inrecentyearsduetotheeconomicadvantageofscale(Richter,2024).
The Compute Supply Chain
| Compute                        |         |                    | Compute        |     | Compute     | Deployment       |
| ------------------------------ | ------- | ------------------ | -------------- | --- | ----------- | ---------------- |
| Production                     |         |                    | Provision      |     | Usage       |                  |
| Integrated Device Manufacturer |         |                    | Big Tech Firm  |     |             |                  |
| Fabless                        | Foundry | OSAT               | Cloud Provider |     | AI Company  |                  |
|                                |         | A s s e m b ly ,   |                |     | etupmoC A I |   D e s i g n ,  |
Design Fabrication T e s t i n g ,   a n d   spihC D a t a   C e n t er   D a ta   C e n t er  Tr a i n in g ,   a n d
|     |     | P a c k a g i n g | C o n s t r u c t io n | O p e r a ti o | n E | n h a n c e -
 |
| --- | --- | ----------------- | ---------------------- | -------------- | --- | -------------- |
ment AI model
| E le c t r o n i c |   D e s i g n   S e m i c o n d u c | t o r   | L a n d ,  C o o l i n g , |     |     |     |
| ------------------ | ----------------------------------- | ------- | -------------------------- | --- | --- | --- |
P o w e r ,  W a t e r,
A u t o m a t i o n   M a n u f a c tu r i n g   Materials IT   i n f r a s t r u c tu r e ,  C o n n e c ti v i ty Algorithms, Data
| S o f tw a r e ,   | C o r e   I P E q u i p m e n | t   | N e t w o r k i n g    |     |               |     |
| ------------------ | ----------------------------- | --- | ---------------------- | --- | ------------- | --- |
|                    | Inputs to Chip Production     |     | Inputs to Data Centers |     | Inputs to AI  |     |
“Computing Power and the Governance of Artificial Intelligence”  Sastry, Heim, Belfield, Anderljung, Brundage, Hazell, O'Keefe, Hadfield et al., 2024
Figure3: Thecomputesupplychainincludingcomputeprovidersinthemiddle. Liketheproduction
ofstate-of-the-artAIchips,computeproviders’marketsharesareconcentrated. (FigurefromSastry
etal.(2024).)
Bycapitalizingontheirpositionasinfrastructureproviders,computeproviderscanplayakeyrolein
regulatingAIcompanies. Leveragingcomputeinthismannercanhelpreduceregulatoryburdens
becauseeachcomputeprovider(i)typicallyservicesmultipleAIfirms,12therebystreamliningthe
regulatoryprocess,and(ii)screenspotentialtargetsforregulationbythescaleofcomputeusage
(whichcanbesupplementedbyfurthercriteria),whetheritisusedfortrainingordeployment. This
follows the model of how financial institutions operate under KYC schemes (Financial Crimes
Enforcement Network, 2005; 2024; Egan & Heim, 2023), although compute providers with the
capacityforfrontierAIdevelopmentanddeploymentaremuchfewerinnumberthanbanks.
12Thesizeofthecustomerbaseofcomputeprovidersvariessignificantly.Typically,computeprovidersoffer
theirservicestoawiderangeofentities,withmostusagefallingoutsidethescopeofourprimaryconcerninthis
paper(seeSection1).Nonetheless,ouranalysisalsoincludeslargecomputeownerswhoexclusivelyusetheir
resourcesinternally.Forexample,amajortechnologycompanycannotcircumventtheguidelinesproposedin
thisdiscussionbymerelycategorizingitsusageas“internalprovisions”ornotidentifyingitselfasa“customer.”
ThisapproachensurescomprehensivecoverageofallrelevantformsofcomputeprovisionforfrontierAI.
11

2.2 GovernanceCapacities
ComputeproviderscanfacilitateeffectiveAIregulationviafourkeycapacities. Theycanbesecurers,
recordkeepers,verifiers,and,insomecases,evenenforcers(Section2.2andFigure4).
|          | Governance    | Capacities   |             |
| -------- | ------------- | ------------ | ----------- |
| Security | RecordKeeping | Verification | Enforcement |
Helpingprovidephysical Theselectivecollection, Activelyverifyingcustomer Restrictionorlimitationof
andcybersecuritymeasures organization,and identities,specificactivities, computeaccessto
tosecuretheAImodel, maintenanceofhigh-level andhigh-levelAIsystems’ customersorworkloadsfor
relatedintellectual informationofacompute properties. non-compliantcustomers.
| property,andpersonaland | provider’sinfrastructure |     |     |
| ----------------------- | ------------------------ | --- | --- |
| confidentialdata.       | usage,suchasacustomer’s  |     |     |
computeusagedata.13
Enables
Enablessharedsecurity IncreasesvisibilityintoAI Ensuresthatthe Directlyimpactsthe
standardstoprotectthe development,links deploymentand capabilityofcustomersto
publicgood,suchas customersandtheirusage developmentofAIsystems developordeploy
safeguardingcritical toreal-worldactors,and adheretoregulationsor advancedAIsystems,
infrastructureandhelping enablespost-incident companypoliciesand ensuringadherenceto
preventmodeltheft. attributionsandforensics. reportedproperties. rules.
Examples
HelppreventIP(e.g., Obtaininsightsinto Confirmcompliancewith Restrictaccessto
algorithms),modelweights, nationalcomputeuse mandatoryreportingover customerslackinglicenses
andtrainingdatafrom trendsforpolicy trainingcompute asanAIdeveloperfortheir
beingstolenbymalicious formulation,suchas thresholds. system.
| actors.              | computedistribution(e.g., |                        |                  |
| -------------------- | ------------------------- | ---------------------- | ---------------- |
|                      | USNAIRR).                 | Verifycompliancewith   | Refusetodeployan |
| Helppreventattackson |                           | datausageguidelinesfor | unlicensedor     |
large-scaledeploymentsof Enablemonitoringfor frontierAItraining. non-compliantAImodel.
| foundationalmodelsthat | suspectedviolationsofthe |     |     |
| ---------------------- | ------------------------ | --- | --- |
couldshutdowndozensof reportingrequirements Verifyifthedeployed DisableAIsystemsthat
criticalservices underExecutiveOrder frontierAIsystemhasan demonstrateactivitythatis
nationwide. 14110. adequatelicenseor undesirable,uncontrollable,
|     |                         | certification. | orinviolationof           |
| --- | ----------------------- | -------------- | ------------------------- |
|     | Collectinformationonthe |                | regulations(e.g.,computer |
|     | environmentalimpactofAI |                | worm-likeAIsystem).       |
computeuse.
Table1: Summaryofthekeygovernancecapacitiesthatcomputeproviderscanenable.
These governance capacities are distinct from but related to obligations to report information to
governments. In many cases, it will be appropriate for compute providers to collect and retain
informationinternallyandonlyprovideinformationtogovernmentsinresponsetoexistinglegal
authorities(forexample,identifiedviolationsofsanctions,orinresponsetolegalwarrants). Inother
cases,forexample,whereacustomerisundertakingalargetrainingrun,regulatorsmayseefitto
mandateproactivereporting. Recordkeepingcanensurethatcomputeprovidersareawareof,and
abletocomplywith,broaderregulationstoincreasevisibilityandoversight.
2.2.1 I.Security
Computeproviders,ascustodiansofsensitivedataandAI-relatedIP,haveadistinctcapacityfor
governingandimplementinginformationsecuritymeasuresthatprotectAIsystems.
13Focusingonessentialdatathatinformswithoutcompromisingprivacyandconfidentiality.
12

I. Securing
Provider takes physical and cybersecurity
measures to secure the AI model, related Compute Provider
intellectual property, and personal and
confidential data.
AI Company
II. Record   Provider selectively collects, organizes,
and maintains high-level information on
Keeping
the AI Company's infrastructure usage,
focusing on essential data that helps Compute Provider
validate regulatory compliance without
compromising confidentiality or privacy.
Regulator
AI Company
A Regulator may require information from
the Provider through law/regulations in
accordance with regulations.
III. Verification
Provider actively verifies the AI   Provider shares information in
Company’s identities, specific Compute Provider case of a violation or in response
activities, and AI Systems' high-level to Regulator request.
properties for compliance.
Regulator
AI Company
Regulator can investigate the AI Company in case of a violation.
IV. Enforcement
Provider identifies an AI   Provider takes predefined actions, such as
Company's violation Compute Provider reporting the violation to an Regulator
(e.g., via verification). and/or restricting or limiting the AI
Company’s access to compute.
AI Company Regulator
Figure 4: Overview of the different governance capacities and how they relate to three actors:
customers(theAIdevelopersanddeployers),computeproviders,andregulators.
FrontierAImodelsrepresentconsiderablefinancial,computational,researchinvestments,andpower-
fultoolsthatcouldbemisusedforfinancialorpoliticalgain;thismakesthemhighlyattractivetocyber
attackersandotheradversarialactors(Cottier,2023;Sevillaetal.,2022). Securitymeasuresshould
extendbeyondsafeguardingmodelweightstoincludetheprotectionofthemodel’sarchitecture,its
algorithmicinnovations,trainingdata,andotherrelatedintellectualproperty(IP)(Nevoetal.,2023).
Therefore,itisimportanttotakerobustcybersecuritymeasuresproportionaltotheserisks. These
measurescouldbelegallymandated,aswiththephysicalandcybersecurityprecautionscurrently
requiredfromdatacentersthathandleHIPAA-andITAR-complianthealth(OfficeforCivilRights,
2016)anddefensedata14,aspreventingthetheftofpotentiallydual-useAIintellectualpropertyand
disruptiontocriticalAIinfrastructurearemattersofpublicgood.15
14ITAR compliance requires arms-related data to be secured from foreign persons. There is no formal
certificationprocessforcloudproviders,althoughmanychoosetobeauditedbyathird-partyorganization
certifiedundertheFederalRiskAuthorizationManagementProgram(FedRAMP)(CodeofFederalRegulations,
2024).
15Suchregulationscouldbeenforcedbycharteringorregistration(forexample,firmscannotacceptfederally
insureddepositsunlesscharteredasabank,creditunion,orthrift)(CongressionalResearchService,2023),or
13

I. Securing
Provider takes physical and cybersecurity
measures to secure the AI model, related Compute Provider
intellectual property, and personal and
confidential data.
AI Company
II.F Rigeucroerd5 : Thesecu  r  iPtryovmideer asesleucrtieveslyi cmollpecltes,m orgeannitzeeds, bycomputeproviderstohelpprotectAIcompany’s
Kemeopdinelgs,intellectualparnod pmeairnttyai,nsa hnigdh-lcevoenl ifinfdoremnattiioanl ond ata.
the AI Company's infrastructure usage,
focusing on essential data that helps Compute Provider
validate regulatory compliance without
compromising confidentiality or privacy.
Suchameasureshouldtakeintoaccountexistingindustrypractice: Large-scalecRoemgupluatteoprroviders
AI Company
alreadyallocatesignificantresourcestophysicalandcybersecurity,givenstrongbusinessincentivesto
keepclients’sensitivedatasecure(including,insomecases,classifiedgov  e  rAn Rmegeunlattodra mtaay (reLquoihrer i,nf2or0m2at3io)n. from
the Provider through law/regulations in
WhenmultipleAIfirmsutilizeasinglecomputeprovider,theyinherentlybeancceofirdtanfcreo wmith trhegeulpatrioonvs.ider’s
comprehensive physical and cybersecurity measures, which benefit from the economies of scale
IIIa.n Vdesriigfinciafitcioanntinvestment. Nevertheless,computeprovidersremainvulnerabletomaliciouscyber
actorsandcanbethes  u  b C Pr o joe m vci p dt a es n r y oa ’s cf t i i d vs e eu n ly t c i v t c i e e er s i , fs i s es p sf e tu c h if le i c Ac Iy berat C ta o c m ks p ( u G te at l P a r n o , v 2 i 0 d 2 e 3 r ;Va  n  c Pi a ar s on e v ,i o d f 2 e a r0 v s2 i h o a4 la re) ti s. o i n nT f o oh r r m i e n a r pt e ioo sp nt o ei n nn s e t ial
forfrontierAItobesto
a
l
c
e
ti
n
vi
,
tie
m
s,
i
a
s
nd
u
A
s
I
e
S
d
y
,
ste
o
m
r
s'
t
h
o
igh
b
-l
e
ev
c
e
o
l
mecriticallyimportantinfrtao sRterguulcattourr reeq,umesta.ywarrant
thedevelopmentofstropnrogpeerrtiess efocru cormitpyliarneceq.uirementsforthecomputeprovidersthattrainanddeploy
them. ThisnecessitywasreflectedinthevoluntaryWhiteHouseCommitments(RTehgeuWlathoirteHouse,
AI Company
2023a)andtheHiroshimaInternationalGuidingPrinciplesforAI,whichadvocateforstrengthened
safeguardsinthisdomain(EuropeanCommission,2023a;b).
Regulator can investigate the AI Company in case of a violation.
Itiscrucialtoacknowledgethattheresponsibilityforensuringinformationsecuritydoesnotrestsolely
withcomputeproviders. Theefficacyoftheirsecuritymeasuresrequiresrobustsecuritypracticesand
collaborativeeffortsbyAIcompaniesthemselves. Withoutthesecompanies’proactiveengagement
IV. Enforcement
insafeguardingtheiroperatio  n  Psr,otvhideerp idreonttieficest iavn eAIm echanismsimplementedb  y  Pcroovmidperu ttaekeps prroedveifdineedr sacctioonus,l dsuch as
Company's violation Compute Provider reporting the violation to an Regulator
proveineffective. Therefore,t(he.ge.s, veiae vfefrioficrattsiona)r.enotsubstitutivebutrathercoamndp/olre rmesterinctitnagr oyr, liwmitiitnhg tbheo AtIh
Company’s access to compute.
computeprovidersandAIcompaniessharingresponsibility.
AI Company Regulator
2.2.2 II.RecordKeeping
Recordkeepingdescribestheprocessofcollecting,organizing,andmaintaininginformationona
computeprovider’scustomersandtheirinfrastructureusage.Computeprovidersareinherentlyrecord
keepersbyvirtueoftheirroleandtechnicalnecessity. Theystoreandprocessvaluabletechnical
data during large AI deployments and training runs for billing purposes, resource management,
andservice-levelagreementtracking(seeSection3formoredetail). Providedthatrobustprivacy
protectionsareinplace,thisinformationcouldbeusefultoregulatorsinoverseeingthedevelopment
ofadvancedAIsystems. Werecommendthatregulatorsandprovidersfocusonessentialdatathat
informsAIregulationwithoutcompromisingprivacyandconfidentiality(whichwediscussinmore
detailinSection5.2).
Record keeping serves three main purposes: it allows more visibility into the developments of
AIgenerally,helpslinkcustomersandtheirusagetoreal-worldactors,andenablespost-incident
attributions and forensics. First, it provides visibility into AI developments, which is important
formonitoringthetrajectoryofAIsystemsandtheircomputerequirementsacrossvarioussectors
(Sastryetal.,2024). Aswehaveseendemonstratedbyrecentnationalcomputeinitiatives(Centerfor
OpenScience,2019;UKDSIT&Donelan,2023;TheEuropeanHighPerformanceComputingJoint
Undertaking,2023;U.S.NationalScienceFoundation,2024),computeprovisioncanbeamechanism
toguideAIdevelopmentandformulatepoliciesforabeneficialdistributionofcomputeresources
(Besirogluetal.,2024;Sastryetal.,2024). Bygatheringaggregatedandanonymizedcomputeusage
data,governmentsarebetterpositionedtoformulatepoliciesthatmitigateunequalaccess,reduce
marketmonopolization,addresspotentialnegativeimpacts,andboostbeneficialinnovationsaligned
withnationalobjectives(Sastryetal.,2024).
tiedtoalicensetoacquirespecializedAIcomputehardware,asisalreadyinplacefortheexportofcertain
equipmentfromUScompanies(AMD,2024).
14

I. Securing
Provider takes physical and cybersecurity
measures to secure the AI model, related Compute Provider
intellectual property, and personal and
confidential data.
AI Company
II. Record   Provider selectively collects, organizes,
Keeping and maintains high-level information on
the AI Company's infrastructure usage,
focusing on essential data that helps Compute Provider
validate regulatory compliance without
compromising confidentiality or privacy.
Regulator
AI Company
A Regulator may require information from
the Provider through law/regulations in
accordance with regulations.
Figure 6: The compute provider collects and manages essential usage data on the AI company
III. Verification
anditsinfrastructureusage,focusingonkeydatathathelpsvalidateregulatorycompliancewithout
comprom  is  iC P n r o o mg vi pp d a e rn r iy v a ’s c a t i i dc v e e yn l . y t i v tTi e e r hs i , f i i s e sp s e f t c h aif e ci c A i l I itatesg C r o ea m te p r u tr t a e n P s r p o a v re id nc e y r into   Ac P a r sI o e v a i o d df e av r va s i h on a la r c e tei s o m i n n f oe o r r n m int a sr t e, io spc n o o i n n us el dlinkcompute
activities, and AI Systems' high-level to Regulator request.
usetoreal-pwrooperrltdiesa focrt coormsp,liaanncde.enableseffectivepost-incidentresponseandforensics.
Regulator
AI Company
Second,recordkeepingenablescomputeprovidersandregulatorstoidentifytheircustomersandthe
correspondinglegalentit  ie  Rse(gKulaYtoCr c)an. Winveistthigatthe tehed AeI vCeomloppanmy ien ncatseo off af rvoionlattiioenr. AIregulations,itwilllikely
becomenecessarytoverifytheidentityofcomputecustomersutilizinglargeamountsofcompute
andensurethattheyhavethenecessarycertificationsandsafeguardsinplace,iftheyplantobuild
IV. EnforcemeanntddeployadvancedAIsystems. Furthermore,countriesmaywishtoenforceexportcontrolson
Provider identifies an AI   Provider takes predefined actions, such as
compute,restrictinCgomtphaenys'sa vlioelsatioonf dataceCnotemrpcauptaec Pitryotvoidaecrtorswrietphoritmingp threo vpioelratisoon utor acne Rsegouflaftourn ding(e.g.,
(e.g., via verification). and/or restricting or limiting the AI
terroristorganizations)ororiginatingfromsanctionedgeographiCcoamlpaanrey’as sac(ceUssS to BcoImSpu&te.USDOC,2023;
Heim&Egan,2023).
AI Company Regulator
Third, andrelatedtocustomerverification, recordkeepingenablespost-incidentattributionsand
forensics(O’Brienetal.,2023).16 Informationaboutdevelopersandtheiractivitiesiscriticalfor
assigning liability or enhancing existing systems in the aftermath of incidents. This is akin to
mandatoryrecordkeepinginthefinancialandtelecommunicationsindustriesforlawenforcement
purposes(legislation.gov.uk,2014;U.S.SecuritiesandExchangeCommission,2003). Wepropose
carefullegislationthatrequirescomputeproviderstomaintainrelevantrecordswhiletakinginto
accountprivacyconcernsandtheregulatoryburden. Thisisespeciallyimportantincasesofpotential
unlawfulusewherethedevelopersmaynotkeepadequaterecordsintheabsenceoflegislation. For
example, high-levelcomputeutilizationdatacouldbemadeavailabletoregulatorsuponrequest,
whiledetailedretainedinformationmaybekeptconfidentialunlessrequiredforenforcementorlegal
proceedings.
Incontrasttoverification,whichisintroducedbelow,recordkeepingdoesnotrequireactiveprocess-
ingbythecomputeprovider. Instead,itdescribesthecollectionofspecificdata,whichisalready
happening to some extent, to make more information available to governments. For example, it
couldinformnationalpolicydecisionsandstrategies(Whittlestone&Clark,2021),andhelpprevent
andrespondtoseriousincidents(whererequiredunderwarrantsand/orbyregulation). Theuseof
aggregated and anonymized compute usage statistics could offer valuable insights into trends in
AIdevelopmentandcorrespondingcomputedemands(e.g.,tolearnmoreabouttheimpactsofthe
computedivide(Ahmed&Wahed,2020;Besirogluetal.,2024)). Thisapproachallowsregulatorsto
understandandrespondeffectivelytotheevolvingneedsoftheAIeconomywithoutencroaching
upon the privacy and confidentiality of companies. This could operate on a need-to-know basis,
ensuringthatonlypertinentinformationisgatheredandutilizedinawaythatminimizesregulatory
burden.
Furthermore,transparencyrequirementsforenvironmentalaccountability,particularlyinthecontext
ofcomputeproviders’substantialenergyconsumption,havebeensuggested(OECD,2022). Mandat-
ingreportsontheenvironmentalimpactofcomputeproviderscouldequipregulatorybodieswiththe
insightsnecessarytofulfillenvironmentalobjectives. TheEUalreadyhasimplementedreporting
requirements.17 Concurrently,numerouscomputeprovidersarealreadyadvancingtowardgreater
16AnexampleofthiscouldbeintheeventofanAIsystemmalfunctioningandcausingfinanciallossor
physicalharm,recordkeepingallowsforthetraceabilityoftheAI’sdevelopmentanddeploymentprocess,
helpingtoidentifytheoriginofthefault(forensics)andpartiesresponsible(attribution).
17“Underthedirective, ownersandoperatorsofdatacenterswith500kilowattsormoreofinstalledIT
capacitywillneedtoreporttheir2023energyperformancebyMay15,2024. Thatincludesstatisticsabout
15

I. Securing
Provider takes physical and cybersecurity
measures to secure the AI model, related Compute Provider
intellectual property, and personal and
confidential data.
AI Company
environmentaltransparencyandhavepledgedtoundertakeclimateinitiatives. (Amazon.com,Inc.,
2024;MicrosoftAzure,2024a;GoogleCloud,2024b).
II. Record 2.2.3   PrIoIvIid.eVr eserleificticvaeltyi coonllects, organizes,
and maintains high-level information on
Keeping
the AI Company's infrastructure usage,
Compu
fo
t
c
e
usi
p
n
r
g
o
o
v
n
i
e
d
ss
e
e
r
n
s
tia
c
l
a
da
n
ta
a
th
ls
a
o
t he
a
lp
c
s
t ively vCeorimfypcuutseto Pmreorvicdoemrpliance with regulatory requirements,
providvianlgidaAteI refigurmlatooryv ceormsipgliahntc.e Swiimthoiulat rtobanksandotherfinancialintermediaries,computeproviders
compromising confidentiality or privacy.
canactivelyverifytheidentityofcustomersandkeycustomeractivities,checkingthattheproperties
ofAIsystemsbeingdeployedordevelopedmatchcustomerreporting. ThRisemguiglahttoinrcludeverifying
AI Company
thetypeofcomputationalworkloadrunbythecustomer(e.g.,traininganAImodel,ordeployinga
modelatscale)aswellasclaimsaboutthetotalamountofcompu  t  eA uRseegudl,atoorr mthaey rteyqpueireo inffodramtaatiuons efrdomin
thetrainingprocess.18 t
a
h
c
e
c o
P
r
r
d
o
a
v
n
i
c
d
e
e
w
r t
i
h
th
r o
r
u
eg
g
u
h
l
l
a
a
t
w
io
/
n
r
s
e
.
gulations in
III. Verification
Provider actively verifies the AI   Provider shares information in
Company’s identities, specific Compute Provider case of a violation or in response
activities, and AI Systems' high-level to Regulator request.
properties for compliance.
Regulator
AI Company
Regulator can investigate the AI Company in case of a violation.
Figure7: ThecomputeprovideractivelyverifiestheAIcompany’sidentities, specificactivities,
IV. Enforcement
and/orproperti  e  s Pr o o f vi A de I r i s d y en s t t i e fi m es s an f o AI r regulatorycompliance.   Provider takes predefined actions, such as
Company's violation Compute Provider reporting the violation to an Regulator
(e.g., via verification). and/or restricting or limiting the AI
AswewilldiscussinSection3,someofthesecapabilities,suchasCoidmepnantiyf’sy aicncgessw toh ceotmhpeurtea. customer
istrainingordeployinganAImodel,canlikelybeimplementedusingexistingdatacollectedby
AI Company Regulator
computeproviders. Providerscouldusethisinformationtocatchregulatoryviolations,including
breachesofmodeltrainingrequirements,whereindevelopersavoidreportingrequirementsandthe
unauthorizeddeploymentofAImodelsatscale.
Verificationrulesshouldbalancebetweenregulatoryrequirements,customerprivacylaws,andsafety
considerations,similartorecordkeepingpractices. Spotchecks(includingthosetriggeredbyreports
oreventsthatraisesuspicion)maybeadequateforlessriskyactivities,whilecontinuousmonitoring
toensurethatcustomer-submittedrecordsareaccuratemaybemandatedforriskierones. Providers
canthencheckifmandatedoradequateriskpracticesareapplied. AIsafetyregulationscouldbe
appliedonlytothoseusinglargeamountsofcomputeandwaivedforsmallercustomers. Additional
factorsmaywarrantfurtherexamination,likeahistoryofnon-complianceorinclusiononrestrictive
listsliketheUSDepartmentofCommerce’sEntityList,whichservestoprotectnationalsecurity
interests. Thestandardizationandaggregationofreportingprocessesacrossprovidersiscrucialfor
ensuringeffectivecross-providerverification. ThisuniformitypreventsAIdevelopersfromevading
regulationsbysplittingtheirtrainingordeploymentactivitiesamongmultipleproviders.
Verificationbecomesvitalincasesofbehaviorthatmayindicatenon-compliance,suchasafailureto
reportdetailsofatrainingrunmandatedbyregulationsliketheAIExecutiveOrder. Forexample,
if there is credible evidence of a sophisticated AI model having been trained, regulators could
requestcertainverificationsfromcomputeproviderstoconfirmthatmodeldevelopersorproviders
areincompliance. Thisapproachissimilartoselectivetaxaudits, providingtheregulationwith
more enforcement capability (Advani et al., 2023). Even though immediate action might not be
taken,havingaccesstosuchinformationallowsforinspectionifnecessary,especiallyinresponse
tosuspiciousactivity. Computeproviderscouldrespondtosuchregulatoryrequestsbyverifying
customeractivitiesandprovidinganadditionalcheckthatmodeldevelopersarefollowingrules. This
processmayinvolveaskingcustomerstoprovidejustificationsorevidencefortheiractivitiesinthe
samewaythatfinancialinstitutionscaninquireaboutsuspicioustransactionsfromtheirclients.
installedpower,incomingandoutgoingdatatraffic,totaldatastoredandprocessed,energyconsumption,power
usage,temperaturesetpoints,wasteheatutilization,anduseofrenewableenergy.”(Korolov,2023)
18Hardware-enabledmechanismsforverificationandenforcementofgovernanceregimesarediscussedin
Aarneetal.(2024)andKulpetal.(2024).
16

Unlikerecordkeeping,verificationdemandsmoreproactiveengagementfromcomputeproviders.
Verification could span a wide range of different specific activities and may include confirming
theidentitiesofcustomerswhousesubstantialcomputeresourcesorcheckingthattheworkload
being executed matches their declared type. In complex cases (such as frontier model training)
I. Securing
or d   irPerocvtidveri toaklaest ipohynsiscaol afndr ecypboerrsetciunrgity requirements, the compute provider may flag the case and refer
measures to secure the AI model, related Compute Provider
itdirectlytoregulators. Itisimportanttonotethatseveralopenquestionsregardingprivacyand
intellectual property, and personal and
technciocnafidlefnetiaals diabtai.litymustbeinvestigatedandpotentiallyaddressedpriortoimplementation. These
considerationsarediscussedintheSection5.
AI Company
Forillustrativepurposes,imagineascenarioinwhichregulationsrequireAIdeveloperstoreporttheir
computeusage,ornotifyagovernmentpriortotrainingamodelaboveacertaincomputethreshold,
ashasbeenoutlinedintheAIExecutiveOrder. Insuchcases,anAIdevelopercouldberequired
II. Record topr  o  Pvriodveideirn sfeolerctmivealyt icoolnlecatsb, oorugatncizoesm, puteusagetotheprovider. Thisallowscustomerstodemonstrate
Keeping that thaendir mcaiontmainps uhitgihn-lgevepl oinwforemratwiona osn employed for specific purposes, such as training several smaller
the AI Company's infrastructure usage,
modelfsocruasitnhg eonr etshseanntiaal dsaitan tghalet hlealprsg ermoCdoeml,wpuhtiech Pmroivgihdtebresubjecttodifferentcompliancestandards.
validate regulatory compliance without
Theprcoomvpirdoemrisitnhg econnfcidheentciaklisty tohr aprtivtahcye. actualusageisconsistentwiththedeveloper’srepresentations. If
inconsistenciesareidentified,thecomputeprovidercanflagtheseeventsforfurtherinvestigation
Regulator
andcompliaAncI eCcohmecpkasn.yThisarrangement,whichusescomputeprovidersasanintermediary,helps
minimize regulatory burdens on the AI industry. Similarly, a compute provider could require a
A Regulator may require information from
modeldevelopertoprovideproofthattheyhaveappropriatelynthoet Pifiroeviddetrh tehroguoghv elarwn/mregeunlattioonfs ian threshold-
accordance with regulations.
exceedingtrainingrunpriortothecomputeproviderallowingaccesstorelatedcompute.
III. Verification
2.2.4  I  VPr.ovEidnerf oacrticveelmy veernifites the AI   Provider shares information in
Company’s identities, specific Compute Provider case of a violation or in response
activities, and AI Systems' high-level to Regulator request.
Computeprpoproervtieisd feorr scocmapnlianacles.oaidregulatoryenforcement. ByvirtueofcontrollingtheAIdatacenters
themselves, providers have the ability to directly deny access toRreugleu-lbarteoarking customers, and,
AI Company
therefore,preventthecustomerfromdevelopingordeployingcertainkindsofAIsystemswiththat
provider. Thecomputeprovidermightlimitcomputeresourcesdevotedtoworkloadsthatraisered
flagspendingfurtherinv   eRsetiggulaattioor nca.n Sinivmestiilgaatrel yth,e rAeIc Coormdpakney einp cianseg oaf na dviovlaetiroinfi.cationprocessescouldtrigger
regulatoryenforcementmeasuresbyotheractors,suchastheDepartmentofJusticeintheUS.
IV. Enforcement
Provider identifies an AI   Provider takes predefined actions, such as
Company's violation Compute Provider reporting the violation to an Regulator
(e.g., via verification). and/or restricting or limiting the AI
Company’s access to compute.
AI Company Regulator
Figure 8: The compute provider detects violations by the AI company, e.g., via the verification
process, and can take appropriate enforcement actions, such as restricting or limiting access to
compute.
Inadditiontoassistinggovernmentalenforcement,computeproviderscanenforcetheirtermsof
service (ToS). By expanding their ToS to include stipulations on AI development and usage to
promotesafety,providerscanautonomouslyenforcecompliance. Thisself-regulationapproachgoes
beyondmerelyreactingtogovernmentregulations;itcouldbeanactivepromotionofresponsibleAI
practices—reflectingtheproviders'commitmenttoethicalstandardsinAIdevelopment.
Direct enforcement by compute providers can come in multiple forms. On the most basic level,
regulation couldbecraftedto requireprovidersto refrainfromprovidingcomputetodevelopers
totrainamodelaboveacertainthresholduntilthedeveloperprovestheyhavetakenappropriate
regulatory steps, such as notifying the government of a large training run or obtaining relevant
approvals. Providerscouldalsohelpregulatorsenforcerulings(e.g.,whenalicenseisdenied,or
whenagovernmentistryingtopreventamaliciousactorfromaccessingcompute)orautomatically
denytheexecutionofAIsoftwaredependingonwhetherthemodelisapproved. Morefine-grained
restrictions,suchasslowingaccessorlimitingcertainworkloadsuntiltheproperregulatoryapprovals
areissued(similartofinancialserviceproviderstemporarilyflaggingatransactionforfurtherreview),
could also be enforced. Compute providers could monitor the activity of customers using large
17

amounts of compute that have stated they are not engaging in model training for signs they are
circumventingthetypesofrequirementslaidoutabove.
Enforcementworksmosteffectivelyinconjunctionwithverification. Detectedviolationscanbe
promptlyacteduponthroughthecomputeproviders'capabilities. However,itiscrucialtokeepthese
twocapacitiesdistinct. Enforcementactionscanbebasedoninformationbeyondwhatisverifiedby
computeproviders,forexample,inresponsetointelligenceprovidedbylawenforcementagencies.
Likewise, violationsidentifiedthroughtheverificationprocessmaybeaddressedthroughmeans
otherthanrestrictingcomputeaccess. Forexample,ifacustomerisfoundtobeoutofcompliance
withexistingregulations,orthecomputeprovider’sToS,theprovidercanrestricttheiraccesstothe
computationalresourcescompletelyandreportthemtotherelevantauthorities. Theprovidercan
alsouselessonerousenforcementmechanisms,e.g.,turningofftheworkloadofconcern,reducing
theamountofavailablecomputeresources,orfiningtheactor.
3 TechnicalFeasibilityofComputeProviders’GovernanceRole
Thissectionexaminesthetechnicalfeasibilityofactivitieswithineachofthegovernancecapacities
introducedintheprevioussection.
Weassessfeasibilityinthecontextofthetechnicalcapacitiesavailabletocomputeproviderstoday,
andthecapacitiesthatcouldforeseeablybedeveloped. Anoverviewofthetechnologystackavailable
tocomputeproviderscanbefoundinAppendixAandisrecommendedforreadersunfamiliarwith
datacentertechnology.
Keytermsusedinthissection
Workload: Acomputationaltask,definedbyaspecificinstanceofsoftware(i.e.,writtenor
compiledcode)thatwillberunonahardwareconfiguration. Forexample,traininganAI
modelisatypeofworkload. Theinputdatatotheworkloadmayormaynotbeknownin
advance.
Operation(OP):Asinglecalculationrunoncomputerhardware,typicallyamultiplication
oradditionoftwonumbers. AIworkloadsusuallyinvolvelargenumbersofmatrix-multiply
operations, which are implemented as repetitive multiplications and additions (known as
multiply-accumulate).
AI accelerator: A hardware device (typically a specialized chip) designed for fast and
efficient execution of AI workloads. Typically AI accelerators excel at simple, parallel
calculations,whichcanalsobeusefulforgraphicalandscientificcomputingworkloads. This
isanumbrellatermforbothcurrenthardwareparadigms(suchasGPUsandTPUs),aswell
asnovelfuturedesigns.
Node: A single computer within a data center. Each node is a distinct unit with its own
processing power, memory, and storage, capable of running a workload by itself, or in
collaborationwithothernodes. EachnodemaycontainmultipleAIaccelerators.
(Computing)cluster: Agroupoflinkednodesthatcanworktogethertoprocessworkloads.
Typicallyusedforworkloadsrequiringsignificantcomputationalresources,suchaslarge-scale
AItraining.
Datacenter: Afacilitythathostscomputingclusters(orothercomputinginfrastructure)and
providesthesupportinginfrastructureneededtooperatethemefficiently.
Insummary,computeprovidersareresponsibleformaintainingsecurepremises,andphysicaland
networkinfrastructure. Theyalsooperatecontrolsoverthatinfrastructure(atboththehardwareand
softwarelevel)thatallowthemtograntandrevokehardwareaccesstoparticularcustomers,storeand
maintaincustomerdata,trackhardwareperformance,anddebugtechnicalissues. Thesesametools
couldallowcomputeproviderstoengageinsecurity,recordkeeping,verification,andenforcement
forfrontierAIregulation,whilepreservingexistingindustrynormssurroundingconfidentialand
privatedata. Table2mapsthesegovernancecapacitiesontotherelevanttechnicalcapacitiesavailable
tocomputeproviders,andindicatesthecurrentfeasibilityofusingthem.
18

Governance Relevanttechnicalcapacitiesofcompute
Currenttechnicalfeasibility
capacity provider
Physicalsecurity(e.g.,locks,guards,surveillance). Feasible for low-end threats (in a supporting
role).Manycomputeprovidersprovidedecent
Infrastructure-levelsecurity(e.g.,accesscontrols, default levels of physical, infrastructure, and
securefirmware,resourceisolation). networksecurity. Withadequatecustomerin-
vestmentsincybersecurity,thesemeasuresare
Security Networksecurity(e.g.,firewalls,networkauthenti- likelysufficientagainstopportunisticattackers,
cation). butnotagainstwell-resourcedandpersistentex-
pertattackers.
Providingadditionalcybersecurityservices(e.g.,
useraccessmanagement,encryptedstorage).
Datarecordcollectionandmaintenance(e.g.,for Highlyfeasible.Computeproviderscan(anddo)
requiredverificationactivities). collectawidevarietyofrecordsoncustomers
Record andtheiractivities.Theserecordsaretypically
keeping Securingdatarecords(e.g.,encryptionatrestand keptsecure,andretainedforaslongasnecessary
intransit,managingaccess). tocomplywithrelevantregulationsorsupport
internalbusinessusecases.
Identityverification: ensuringacustomerand/or Identityverification:likelyfeasiblewithasuffi-
useriswhotheysaytheyare. cientlyrigorousprocess,focusedoncustomers
accessinglarge-scalecomputeresources.
Workload classification: determining whether a
customerworkloadfallswithinacategoryrelevant Workloadclassification: likelyfeasibleforde-
to regulatory requirements (e.g., training a very tecting large-scale pre-training and inference
largeAImodel). workloads.
Verification
Compute accounting: estimating the number Compute accounting: feasible, with multi-
of operations consumed by a workload (e.g., ple approaches possible for large-scale pre-
to validate compute threshold-based reporting training/inferenceworkloads.
requirements19).
Detailed workload verification: currently not
Detailedworkloadverification:verifyingaspects possible without directly observing customer
of the specific code or data used in a workload code or data. “Confidential computing” tech-
(e.g.,tovalidatewhetheracustomeriscomplying niquescouldchangethis.
withreportingrequirementsforcertainhigh-risk
trainingdata20).
Account-levelenforcement: revokingserviceac- Account-level enforcement: highly feasible,
cesstoparticularcustomers/accounts/users. computeprovidershavebothphysicalandsoft-
waremanagement-basedcontrolovertheirhard-
Enforcement Model-levelenforcement:revokingserviceaccess ware;thisiswidelyused.
whereservicesareusedtodeployparticularmod-
els,orwheremodelsaredisplayingdangerousbe- Model-levelenforcement:currentlynotpossible
havior(e.g.,acomputerworm-likeAIsystem). withoutdirectlyobservingcustomercodeordata.
Thismaybecomepossiblewithsometechnical
effort.
Table2: Overviewofrelevanttechnicalcapacitiesavailabletocomputeprovidersandanassessment
oftheirtechnicalfeasibility.
19Forexample,seethetrainingcomputethreshold-basedreportingrequirementintheAIExecutiveOrder
(TheWhiteHouse,2023b).
20Forexample,theAIExecutiveOrder(TheWhiteHouse,2023b)createsspecificreportingrequirementson
developersformodelsprimarilytrainedwithbiologicalsequencedata.Itmaybecomeusefulforthesekindsof
reportingrequirementstoalsobevalidatedbycomputeproviders,orforcomputeproviderstoofferverification
toolstodevelopers(e.g.,“confidentialcomputing”services).
19

3.1 Security
Computeprovidersusuallyprovidesecurityatcertaintechnologylayers,whereasotherlayersareleft
uptocustomers(GoogleCloud,2023;AWS,2024h;CoreWeave,2023). Thecomputeprovideris
typicallyresponsiblefor:
• Physical security, which includes protecting data center premises with locks, cameras,
guards,andsurveillance.
• Infrastructuresecurity,whichincludesensuringthathardwareisup-to-datewiththelatest
firmwaresecuritypatches,securelydisposingofoldhardware,restrictingphysical/virtual
accesstoinfrastructuretoapprovedpersonnelformanagementandmaintenancepurposes,
andensuringappropriateisolationofcriticalsystemresourcesacrossdifferentcustomers
andworkloads
• Networksecurity,whichincludesoperatingfirewallsandprovidingotherformsofnetwork-
levelsecurityandisolation.
Thesephysical,infrastructure,andnetworksecuritymeasuresaresufficienttoprovidecustomers
withabaselinelevelofinformationsecurity,onethatmanycustomerscouldnotachieveontheirown.
Customersarethengenerallyheldresponsibleforthepartsofthetechnologystacktheyhavecontrol
over, which encompasses many aspects of cybersecurity, including protecting data generated or
collectedbytheirworkloads,ensuringtheiremployeesarewell-trainedinsecuritybestpractices,
and implementing access control policies based on different permission levels. Many compute
providers,especiallylargerproviders,offercybersecuritysoftware-as-a-serviceproductsfortheir
customerstohelpthemimplementthesemeasures;manyoftheseproductsarefreeand/orstandard
withinfrastructureofferings. Theseadditionalservicestypicallyprovidethecustomertheabilityto:
• Securelymanageuseraccesstoresourcesintheiraccount
• Workwithencrypteddatastorageintransitandatrest
• Manageandsecureinbound/outboundtrafficfromnodes
• Definedifferentlevelsofsecuritywithindifferentregionsoftheirinfrastructure
InthecontextofprotectingfrontierAIworkloads,ifacustomerisworkingwithasecurity-conscious
compute provider, and the customer has systematically implemented industry best practices for
cybersecurity,theyarelikelywell-protectedagainstmostopportunisticattackers. However,these
measuresarealmostcertainlyinadequatetodefendagainstwell-resourced,expertattackers,such
asnation-state-backedhackinggroups(alsoknownas“advanced,persistentthreats(APTs)”). Such
threatsareofsignificantconcernforfrontierAI,giventhepotentialeconomicreturnsofmodeltheft,
andrisksofmisuse(Nevoetal.,2023).
AsdiscussedinSection2.2.1,itisthereforeimportanttostrengthensecuritystandardsforfrontier
AIworkloads. InadditiontorequiringstrongcybersecuritystandardsforfrontierAIdevelopers,
regulatorscoulddefineenhancedsecuritystandardsforcomputeproviderswhoofferinfrastructure
capableoftrainingfrontiermodelstoclosesecuritygaps.21
3.2 RecordKeeping
Recordkeepingishighlyfeasibleusingtoolsandmetricscurrentlyavailabletocomputeproviders,
whoalreadycollectawiderangeofdataoncustomersandserviceusagefor:
• Accuratelybillingcustomers
• Marketingnewservicestocustomers
• Maintainingandoptimizingserviceprovision
• Detectingandrespondingtofraud,abuse,securityrisks,andtechnicalissues
21Foranexampleofwhatsuchstandardsmightlooklike, seesecurityrequirementsintheFederalRisk
AuthorizationManagementProgram(FedRAMP).FedRAMPassignsdifferentlevelsofrequirementsdepending
onthesensitivityoftheusecase(FedRAMP,2024).
20

• Complyingwithlegalobligations,suchasfinancialrecordkeeping
Computeprovidersalsosharetheserecordswiththirdpartiesforactivitiessuchas:
• Exchanginginformationwithothercompaniesforfraudprevention,detection,andcredit
riskreduction
• Providingthird-partyvendorswithinformationforpromotionalandmarketingpurposes
• Complyingwithlegalobligations,suchasanenforceablegovernmentrequest
Compute providers typically have well-defined privacy policies around these records, including
specificretentionandsecuritypoliciesbasedonthesensitivityandbusiness-orlegalusecasesfor
differentkindsofrecords. Someofthisdatawilllikelybeusefulforverificationactivitiesrelevantto
frontierAIgovernance. Thespecificdataattributesgenerallycollectedbycomputeproviderscanbe
foundinTable3below,mappedontospecificusecasesforgovernancepurposes. Thisinformationis
basedonconversations,publicdatacollection,andprivacypoliciesavailablefromarepresentative
sampleoflargeandsmallcomputeproviders(AWS,2024g;CoreWeave,2022;FluidStack,2022;
GoogleCloud,2024c;LambdaLabs,2022;Microsoft,2024a).
3.3 Verifying
TherearearangeofverificationactivitiesthatcomputeproviderscouldperformtosupportfrontierAI
governance. Primarily,itwillbeusefulforcomputeproviderstoverifytheidentityofanycustomer
seekingtoaccessahardwareconfigurationcapableofefficientlytrainingafrontiermodel(“identity
verification”),asdiscussedinEgan&Heim(2023)andbyMicrosoft(Smith,2023). Itmayalsobe
usefulforcomputeproviderstoserveasanindependentformofvalidationfordifferentpropertiesof
frontierAIworkloads. Wefindthatdataattributesalreadywidelyavailabletocomputeproviderscan
likelyenablethemtoadequatelyverifytwokeypropertiesofaworkloadthatarecurrentlyhighly
relevantforfrontierAIgovernance:
• The stage of the AI lifecycle the workload fits into, e.g., large-scale model training or
inference(“workloadclassification”)
• Thequantityofcomputeconsumedbytheworkload(“computeaccounting”)
Inthefuture,itmayalsobeusefulforcomputeproviderstoverifyaspectsoftheparticularcode
ordatausedinaworkload,suchasthespecificmodelthatwasdeployed,orthetypeofdataused
to train a model. We describe such activities as “detailed workload verification.” Currently, this
is largely not possible without directly observing confidential customer code or data. However,
withsometechnicaldevelopmentwork,itmaybecomepossibletoimplementwideruseof“trusted
executionenvironments”toallowcustomerstoprovecertainpropertiesoftheirworkloadstotheir
computeprovider(ordirectlytoaregulator)withoutrevealingothersensitivedata(Aarneetal.,2024;
NVIDIA,2023). Wenowdescribeeachofthesepotentialverificationactivitiesinmoredetail.
3.3.1 IdentityVerification
Identity verification (also commonly known as “Know-Your-Customer (KYC)”) is a useful mea-
sure to ensure customers are meeting applicable rules, and enforce relevant penalties. This may
includeensuringparticulardevelopersarereportingrelevantlarge-scaletrainingrunsorenforcing
exportcontrolsthatpreventcertaincustomers(e.g.,thosewithlinkstoforeignmilitary/intelligence
organizations)fromaccessingparticularservices. Inthebeginningof2024,theUSDepartmentof
CommerceproposednewregulationsthatplaceexplicitidentityverificationrequirementsonUS
computeprovidersofferingservicestoforeigncustomers(FederalRegister,2024). Egan&Heim
(2023)discussinfurtherdetailthemechanismsofaKYCschemeforcustomersaccessinglarge-scale
compute,drawingonlessonsfromthefinancialsector.
21

|     | Uses(interms | Involvescollection |     |     |     |
| --- | ------------ | ------------------ | --- | --- | --- |
Currentstateofcollection,
|                   | ofspecific   | ofdatanot     |                        |     |     |
| ----------------- | ------------ | ------------- | ---------------------- | --- | --- |
| Attributecategory |              |               | validation,andpossible |     |     |
|                   | verification | alreadywidely |                        |     |     |
circumvention23
|     | activities) | collected?22 |     |     |     |
| --- | ----------- | ------------ | --- | --- | --- |
Customerinformation
|     |     |     | Compute | providers already | collect a |
| --- | --- | --- | ------- | ----------------- | --------- |
e.g., name, billing address, Identity No,already widerangeofcustomerinformation.
| creditcarddata,IPaddresses,  |              | collected. |                                  |     |     |
| ---------------------------- | ------------ | ---------- | -------------------------------- | --- | --- |
|                              | verification |            | Customerscanpotentiallyspoofmuch |     |     |
| date and time of access, de- |              |            |                                  |     |     |
ofthisdatatotrytoavoididentification.
viceidentifiers,language
| Billing-related technical in- |                |            |                              |              |         |
| ----------------------------- | -------------- | ---------- | ---------------------------- | ------------ | ------- |
| formation                     | Workload       |            | Already                      | collected by | compute |
|                               | classification | No,already | providersforbillingpurposes. |              | Highly  |
e.g.,hardwareconfiguration
requested by a customer, Compute collected. difficultorimpossibleforcustomersto
number of hours that hard- accounting altertoavoidmonitoring.
wareresourcesareused
|     |     |     | Already | collected by | compute |
| --- | --- | --- | ------- | ------------ | ------- |
Cluster-leveltechnicalinfor-
|     | Workload |     | providersforservicehealthmonitoring |     |     |
| --- | -------- | --- | ----------------------------------- | --- | --- |
mation
|     | classification | No,already | and maintenance. | Customers | could |
| --- | -------------- | ---------- | ---------------- | --------- | ----- |
e.g.,powerconsumption,net- collected. modifytheirworkloadstoavoidcertain
Compute
work bandwidth utilization forms of cluster-level verification,
accounting
betweennodes
likelywithperformancepenalties.
Possibletocollectusingexistingtool-
Node-leveltechnicalinforma-
Workload
| tion                       |                |                     | ing, and                          | collected by some | compute |
| -------------------------- | -------------- | ------------------- | --------------------------------- | ----------------- | ------- |
|                            | classification |                     | providers.25                      |                   |         |
|                            |                | Potentially,already |                                   | Customers could   | modify  |
| e.g.,AIacceleratorcoreuti- |                | collected.24        |                                   |                   |         |
|                            | Compute        |                     | theirworkloadstoavoidcertainforms |                   |         |
lization,AIacceleratormem-
|     | accounting |     | of node-level | verification, | likely with |
| --- | ---------- | --- | ------------- | ------------- | ----------- |
orybandwidthutilization
performancepenalties.
Workload
|     | classification |     | Computeproviderscannottypicallyre- |     |     |
| --- | -------------- | --- | ---------------------------------- | --- | --- |
Workload-leveltechnicalin-
tainorinspectthisinformation(byde-
| formation | Compute |                  |                     |           |       |
| --------- | ------- | ---------------- | ------------------- | --------- | ----- |
|           |         | Yes,currentlynot | sign). Confidential | computing | tools |
accounting
e.g.,code,data,hyperparam- collected. couldpotentiallybedevelopedtover-
| eters | Detailed |     | ifyinformationinaprivacy-preserving |     |     |
| ----- | -------- | --- | ----------------------------------- | --- | --- |
|       | workload |     | manner.                             |     |     |
verification
Table3: Anoverviewofthecategoriesofdataattributesavailabletocomputeprovidersandhow
theycanbeusedfordifferentverificationactivities.
Identityverificationofthiskindappearsfeasible, butwerecommendthatpolicymakersconsider
severalstrongcaveats.Asdescribedabove,computeproviderstypicallycollectarangeofinformation
relevanttoverifyingcustomeridentities. Thisincludes(AWS,2024g;CoreWeave,2022;FluidStack,
2022;GoogleCloud,2024c;LambdaLabs,2022;Microsoft,2024a):
22Basedonourcurrentunderstandingandinsightsgatheredfrominterviews,andgivenpubliclyavailable
information.
23Inthiscolumn,wecollectinformationonwhethereachdataattributeisalreadycollected,andifnot,howit
couldbecollected.Wealsolistwhetheritmightbepossibleforcustomerstofalsifyeachdataattributeinorder
toavoidinformationbeingverified.
24Whileexaminingcustomerdataisout-of-scope,collectionandanalysisofcertaintypesofmetadatacould
riskexposingdetailsofthecustomer’sdata.
25SeeWengetal.(2022)andGoogle(2024).
22

• Personalinformation,suchaslegalnames,usernames,emailaddresses,phonenumbers,
andgovernment-issuedidentificationdocuments
• Informationaboutcustomerorganizationsandthepeopleinthoseorganizations
• Financialinformation,suchascreditcardandbankaccountinformation,andtaxidentifiers
• Service-relatedinformation,suchasthelocationsfromwhichusersareaccessingtheservice,
timezones,thetypeofdeviceauserisusingtoaccesstheservice,thelanguageusedon
thatdevice,webcookiesdescribingsitespreviouslyvisited,andIPaddressesusedwhen
accessingtheservice.
Thisequipscomputeproviderswithlargeamountsofusefulinformationforverifyingtheidentity
of customers seeking to access infrastructure sufficient to efficiently run frontier AI workloads.
Becausesuchcustomerswillbydefinitionbefewinnumber,bestpracticesforidentityverification
couldbedrawnfrommoreinvolvedidentityverificationactivitiessuchasthoseconductedinother
industries. Oneexampleisthe“enhancedduediligence”processusedinfinancialsectorsforhigher-
riskcustomersortransactions,whichcaninvolvecommissioningintelligencereportsoncustomers
ortheir“beneficialowners”(theentitythatultimatelyownsorcontrolsthecustomerorganization)
(FinancialActionTaskForce,2003). Thesekindsofmeasuresmaybenecessarytosuccessfully
performidentityverificationinsituationswhereawell-resourcedillicitactorisactivelytryingto
obfuscatetheiridentity.
Inperformingidentityverification,itisimportantforregulatorsandcomputeproviderstobearin
mind potential trade-offs with user privacy and data privacy regulation in different jurisdictions.
Itwouldlikelybeusefulforidentityverificationrequirementstobestandardizedacrossdifferent
jurisdictions. WediscussthesechallengesinSections4.4and5.2.
3.3.2 WorkloadClassification
“Workload classification” describes a scenario where an infrastructure provider is attempting to
classify a workload into a particular category. We will consider, from a frontier AI governance
perspective,whatthesecategoriesmightbe,andhowtheymightbedifferentiated.
First, it is useful to know whether a workload relates broadly to AI. Frontier AI workloads will
generallyalluseAIaccelerators,butnotallworkloadsthatuseAIacceleratorswillnecessarilybeAI
workloads. Forexample,graphicsandscientificcomputingworkloadssometimesuseAIaccelerators.
However,theseworkloadcategoriescanlikelybedifferentiatedusingobservablepropertiesofthe
workload. ExamplesofsuchpropertiesareoutlinedinAppendixBintheAppendix. Withinthebroad
categoryofAIworkloads,thereareseveralsub-categoriesofworkload,correspondingtostagesin
theAImodel’slifecycle,thatareusefultodifferentiatefromagovernanceperspective:
• Design,inwhichresearchersandengineersexperimentwithdifferentmodeldesigns,algo-
rithms,anddatasets.
• Training,inwhichamodellearnsfromalargedataset. Typicallyknownas“pre-training”
todistinguishfromenhancement.
• Enhancement,inwhichatrainedmodelisfurtherrefinedusingasmallerdataset(e.g.,
fine-tuning),sometimesusingtechniquessuchasreinforcementlearning.
• Deploymentinwhichatrainedmodelisusedinanoperationalsetting,e.g.,tomakenew
predictions(“inference”).
Eachofthesecategoriescanbedistinguishedbasedonscale,amongotherattributes. Giventhelarge
scaleofthefrontierAIworkloadsweareinterestedindetectingandclassifying,wecanplaceastrong
initialfilteronwhichspecificworkloadswarrantattention,ignoringthevastmajorityofworkloads
runonacomputeprovider’sinfrastructure. AsdiscussedbySastryetal.(2024),thetrainingstage,
wherecomputedemandsareespeciallyhigh,isanespeciallypracticalstagetomonitor.26
Thesimplestmethodofworkloadclassificationmightbebasedpurelyonthehardwareconfiguration
(in terms of types and numbers of devices) available to a customer. For example, in 2024, if a
customer has requested a hardware configuration involving tens of thousands of AI accelerators,
26SeeSection3.CofSastryetal.(2024).
23

Simplified AI Lifecycle
Development Deployment
Design Training Enhancement
Model
AI Model Enhanced
Architecture
AI Model
“Computing Power and the Governance of Artificial Intelligence”
Sastry, Heim, Belfield, Anderljung, Brundage, Hazell, O'Keefe, Hadfield et al., 2024
Figure9:SimplifiedAILifecycleincludingtraining,enhancement(e.g.,fine-tuning),anddeployment
(i.e.,inference). (FigurefromSastryetal.(2024).)
connectedtogetherusingahigh-bandwidthnetworkfabric,itbecomesmuchmorelikelytheyintend
toengageinlarge-scaletraining,relativetoothercustomers. Combiningthisinformationwiththe
amountoftimethehardwareisbeingusedcantelluswhetheritwaspossibleforacustomertorun
aparticularworkload(e.g.,pre-trainingaboveaparticularscale),whichcouldprovidegroundsfor
amoredetailed investigation. Thesecoarsemethodsarepossible usingdataalreadyavailableto
computeprovidersforbillingpurposes. SeeSection3.3.3belowformoreinformationonthesekinds
ofapproaches.
Moreprecisemethodsforfrontierworkloadclassificationmightinvolvemanuallydefiningsome
technicalcharacteristicsofrelevantworkloads,ortrainingamachinelearningclassifierusingcluster-
andnode-leveltechnicalinformationtopredictwhetheraworkloadfallsintoarelevantcategory.
Compute providers could also collect declarations from customers about the workloads they are
running,andusethatinformationasareferencepointforclassification. Theseapproachesarebased
ontheassumptionthatdifferentkindsofworkloadswillhavecharacteristicandlearnablefeatures. As
anexample,weexpectfrontier-scaletrainingin2024willlikelyhaveseveraldistinguishingfeatures
relativetootherpossibleworkloads. Thesecouldincludethenumberofacceleratorsused(tensof
thousands),thepeakoperationthroughpututilizationofacceleratorsovertime(fairlyconstant),the
patternsofcommunicationbetweenandwithinnodes(followingspecificpatternscorresponding
to different forms of parallelization), and limited outbound/inbound communication to external
networks,suchastheInternet,duringthetrainingrun. Accordingtosixinterviewswithcommercial
computeproviders,includingbothlargeandsmallerproviders,thesekindsofcluster-andnode-level
characteristicsareoftenalreadycollectedandusedtounderstandcustomerworkloadstooptimize
theirservices.27 ResearchreleasedbyGoogle,Microsoft,andAlibabademonstratessomeofthe
waysthistechnicalinformationiscollectedandanalyzedforbusinesspurposes(Jeonetal.,2019;
Tirmazietal.,2020;Wengetal.,2022). Someofthisdatahasbeenreleasedaspublicdatasetsthat
canbeusedtodevelopworkloadclassificationtechniques(Alibaba,2024;Google,2024).
Workloadclassificationtechniquesusingthesekindsofdatahavebeenstudiedindifferentcontexts.
(Tangetal.,2022)introducedthe“MITSupercloudDataset,” containingnode-leveltechnicalin-
formationforover3,000AIaccelerator-basedworkloads. Workloadclassifierstrainedonthisdata
havereached95%accuracyatdistinguishingAIworkloadsacrosstendifferentmodelarchitectures
(Weissetal.,2022).Otherresearchonworkloadclassificationfordifferentkindsofhigh-performance
computingworkloadshasreachedsimilarlevelsofaccuracy(Banjongkanetal.,2018;Teraietal.,
2017),includingclassifierstrainedonlytousedataonpowerdraw(Copos&Peisert,2020;Köhler
etal.,2021).
27InterviewsconductedbetweenOctober2023andFebruary2024
24

However,thereareseveralwaysthesefindingsmaynotberepresentativeforfrontierAIworkload
classificationinaproductionenvironment.First,theauthorsmostlygeneratedlabeleddatabyrunning
workloadsthemselves,whichlikelyinvolvedalevelofstandardizationinsoftwareanddatasetsthat
would be unrealistic for real-world conditions. Second, this research typically involved a small
numberofdifferenthardwareconfigurationsandscales,whereastheseparameterswilllikelyvary
furtherinproductioncontexts. Lastly,evena5%errorratemaybeprohibitivelyhighinproduction,
giventhepotentialconsequencesofreportingafalsepositivetoaregulator.
Computeprovidersofferinglarge-scaleAIclustersarelikelytohavetheexpertisetoaddressthese
technicalchallenges. Indoingso,werecommendthatcomputeproviders—incollaborativeefforts
wherepossible—considerarangeoftechnicalapproachesforclassification,rangingfromsimple
manuallydefinedthresholdsthroughtomachine-learningbasedclassifiers. Thesemethodscould
alsobecombinedwithotherusefuldataandprocesses,suchasbysolicitingcustomerdeclarations
ontheintendeduse/purposeofahardwareconfigurationorworkload,andbyconductingfollow-up
investigationsincaseswhereclassificationconfidenceislow. Box1demonstrateswhataworkload
classificationprocesscombiningtheseelementsmightlooklike.
Box1: AnexampleprocessforfrontierAIworkloadclassification.
1. Thecomputeproviderliststhespecificsetofhardwareconfigurationsandscales
they offer that are sufficient for efficient training of frontier AI workloads (i.e.,
within defined cost/time boundaries). Given that compute providers tend to spe-
cializeinparticularhardwareconfigurations(e.g.,AIacceleratortypesandnode
configurations),thisnumbercouldbequitesmall.
2. Thecomputeprovidercollectslabeledcluster-andnode-leveldataonworkloads
simulatedorrunoneachoftheseconfigurations. Computeprovidersofferingsimilar
hardwareconfigurationsmaybenefitfromcoordinatingtoproducelargerdatasets.
3. The compute provider creates technical thresholds to define relevant workload
categoriesbasedontheiridentifyingcharacteristics,andteststhemonthecollected
data. ThiscouldincludetrainingML-basedworkloadclassifiers. Itmaybethecase
thatasingleclassificationapproachworkswellforarangeofdifferenthardware
configurationsand/orscales,orthatmorespecificclassifiersarerequiredfordifferent
configurations.28
4. Inoperation,foranycustomerseekingaccesstooralreadyusingarelevanthardware
configuration,thecomputeprovidercouldthen:
a. Ensuretheyhaveperformedadequateidentityverification.
b. Collectdeclarationsfromthecustomerontheintendeduseofthehardwarecon-
figuration,and/ordeclarationsonthenatureofanysufficientlylargeworkload
runonthatconfiguration.
c. Validatethesedeclarationsbyrunningautomatedclassificationonworkloads
thatusethatconfiguration,andconductfollow-upanalyseswhereuseful,espe-
ciallyincaseswhereclassificationconfidenceislow.
Thedifficultyofclassifyingworkloadsincreasesifacomputecustomerisactivelytryingtodisguise
thenatureoftheirworkload. Thiskindofobfuscationmaybecomelikelyincaseswhereacustomer
hasastrongfinancial,criminal,orpoliticalincentivetoavoidregulatoryoversight. Suchincentives
arelikelytogrowwhenfrontierAImodelsbecomebothmoreattractiveforcriminalactivitiesand
more economically lucrative. Analogous practices can be observed in the finance sector, where
illicit actors have engaged in “structuring” (breaking up a single transaction into several smaller
transactions)toavoidautomatedtransactionreportingfromtheirbanktotheregulator(Linn,2010).
WediscussandlistthesechallengesinSection5.1.
28Foranexampleofanapproachforsimulatingworkloadsonlargeclusters,seeSliwko&Getov(2016).
25

3.3.3 ComputeAccounting
Weintroduce“computeaccounting”: measurementsandtechniquestoproduceanestimationofthe
amountofcomputeconsumedbyacustomerrunningoneormoreworkloadsonaspecificcompute
cluster. Thesetechniquesarecomparativelysimilartotheprevioussectiononworkloadclassification
(Section3.3.2). However,ratherthanestablishingtheclassofaworkload,computeaccountingaims
to determine its magnitude. Moreover, compute accounting is useful even when the workload is
notclassifiedatall,asanestimateofthetotalamountofcomputeusedbyagivencustomerisan
upperboundforasingle(unknown)workload. Fromapracticalgovernanceperspective,compute
accountingcouldbeusedasaninputtoworkloadclassification, and/orasastandalonemetricto
determinewhetheraparticularworkloadhasexceededacompute-basedreportingthreshold.
Theamountofcomputeusedbyagivenworkloadisausefulmetricfromagovernanceperspective.
InthecontextofAItraining,novelcapabilities(andrelatedrisks)arelikelytofirstemergeinmodels
thatrequirelargeamountsofcompute(Pilzetal.,2024;Sevillaetal.,2022). InthecontextofAI
inference,computeiscorrelatedwiththescaleandprocessingspeedofthedeployment: howmany
copiesofthemodelarebeingrun,andhowfastthemodelisoperating(thethroughput,e.g.,tokens
persecondforLLMs). Insofarasthemodeliscapableenoughtopotentiallycauseharm,thesefactors
couldthenbecorrelatedwithriskandtheneedforenhancedoversight(AppendixIofO’Brienetal.
(2023)).
Moreformally,thetotalcomputingpowerofarentedclusterandhowlongacustomerhasaccessto
itresultsinaquantityofavailablecompute—a“computebudget.” Thecustomeristhenchoosing
howtoallocatethatbudgetacrossdifferentworkloads. Forexample,agivensetofAIaccelerators
couldbeusedforasingletrainingrun,multiplesmalltrainingruns,ormodeldeployment(Figure10).
Incaseswherecomputeisbeingconsumedbyacustomer(asopposedtohardwaresittingidle),the
amountofcomputeconsumedcanbeattributedtoatleastoneworkload. Theadditionofworkload
classificationallowsfractionsofthatusagetobeascribedtoworkloadsofparticulartypes.
Small Small Fine-Tuning Model
Scenario A
Training Run Training Run Experiment Deployment
Fine-Tuning Fine-Tuning
Scenario B Model Deployment
Experiment Experiment
Scenario C Large Training Run
Time / Compute Quantity
Figure10: ThreeexamplescenariosofasetofAIacceleratornodesrunningdifferentworkloads
overtime. Computeaccountingestablishestheamountofcomputeusedovertime,whileworkload
classificationcandifferentiatebetweenthesethreescenariosbymappingcomputeusagetospecific
workloads.
Wecanestimatethecomputebudgetviatwodifferentapproaches:
1. Theoreticalcomputebudgetestimation: calculatedusingtheassumedthroughput(mea-
suredinOP/s)ofthehardwarepotentiallyinvolvedintheworkload,andmultiplyingitby
thetimethehardwareisbeingused.
26

2. Empiricalcomputebudgetestimation: calculatedusingactualmeasurementsfromthe
hardware that can serve as more direct proxies for compute consumption. For example,
aggregatingAIacceleratorcoreutilizationandtime-in-usedataacrossallAIaccelerators
involvedinaworkload,andmultiplyingbythepeakcapacityofeachcore.
Theoretical compute is a derivative of empirical compute, useful for establishing an estimate in
circumstanceswhereempiricalmeasurementsarenotavailable. Asexactcircumstancesandconfigu-
rationsdifferbetweencomputeproviders,notallattributesofboththeoreticalandempiricalcompute
are likely to be observable. However, in practice, both kinds could be used to inform an overall
estimateofcomputeusageforaparticularinstanceofrunningaworkload(Figure11).
st
H
t c o h h
o
r e i i
w
n p A g
m
l I o t a a
u
o c d
c
c m
h
i e n l e
d
g e m
a
r a a
t
o n
a
t r o d y
i
r
s
?
H
c c l
o
o u
n w
m s
o
t
d
e m
m
w
e
r u
a s
i i
n
n s t
i
h
n y
i a c ? a
t o
n
h
t
t
o i
h e
n d
e
g e
r
w
A
p e
r s
r
e u
i o g
c
u
d
v h
h
s
a
i t d i s
t a
n
a
e
s
p g r
a
r
m
’s t o
r
h
t o
d A
i
e
d f
u P
a e
c I
c
?
l
e
t
d
s
t
h
o h
D
l t
a
e i h n
o v
s e k
e t
a r
w
, w m
a
o
o
i
n
e r t h
e n
n e
t o
x e
w
e
d
i t a s
o
w
e
c t
r s
h o
k
i n r k
topology?
o a W ( f d e h d o .g a n it . t - i c o m i h s n u i ) t p l h t p e i o e p p q r l e i f u c o r a a a r n t m t i i t o o i e n t n d y , s ? i n s A e a H I t n w a o c w o i c n r e d k m l i e t v u r r i a c a d t h f u o f i a r c l c p A o o I n H w s a o u c e w m c r e i e m l s e d u r b a b c e t h y i o n r a g ? n ( c o o w r o m u s i I t m e s t h s t a i u d a o n n f e n i o n c t o d a h o d e  t e d i e n e g s) h h a a H a r v d o e c w w u a s a c t m c r o e e m u s d c s e h o r t e o s ?
transmitting? cluster?
Low Level High Level
Measurements Measurements
Figure11: AspectrumofpossiblecomputeusagemetricsforAIworkloadanalysis,fromlow-level
measurements,suchason-chipcalculations,tomorehigh-levelmeasurements,suchasthehardware
available to a customer. Each of these metrics can be synergistically combined to enhance the
accuracyandsensitivityofworkloadclassificationandcomputeaccounting.
Regardless of whether the approach is theoretical or empirical, it will be important for compute
providerstoestimateboththroughput(OP/s)andtotalquantityofoperations(OP).Thisprovides
crucialinformationtodetectcaseswhereacustomerisevadingareportablecomputethresholdby
utilizingmultiplecomputeprovidersoraccountstosequentiallyperformpartialtrainingofamodel.
Inthiscase,thethroughputavailabletothecustomerisnecessarytoidentifythatarateofcompute
usagecorrespondingtoareportablethresholdhasbeenreached,evenifthereportablethresholditself
hasnot. Wediscussthisin5.1.
MeasuringTheoreticalComputeBudget—Theoreticalapproachesmeasurethepotentialfora
certainamountofcomputetobeusedforoneormoreworkloadswithinagiventimeframe. This
is easier to measure than empirical compute, and in the simplest form is equivalent to hardware
resourcesacustomerhasbeenallocatedtoaccesswithinthecluster. Foranygivencomputeprovider,
thenumberofcustomerswithaccesstosufficienttheoreticalcomputetotrainafrontiermodelwillbe
small.29 Thismakestheoreticalcomputeausefulmeasurefordeterminingwhichspecificcustomers
arerelevantforafrontierAIregulatoryregime. Thiscanbecalculatedusingdataalreadyavailableto
computeprovidersforbillingpurposes(Table3). Relevantdataformeasurementofcomputeare:
29Forexample,tomeettheAIExecutiveOrder’sreportingrequirementof1026operationsforatrainingrun,a
customerwillneedaccesstoaround60,000cutting-edgeAIaccelerators(NvidiaH100)for90days,assuminga
utilizationof34%.
27

• Nodeassignment: Computeproviderscanbillcustomersforon-demandnodes(afullor
partial node) at a granularity ranging from seconds to hours (AWS, 2024e), or reserved
nodesrangingfromdaystomonths(AWS,2024f). Theoretically,theusedcomputebudget
canbecalculatedusingthisinformationbysummingthetheoreticalpeakperformanceofthe
AIacceleratorsineachnode,multiplyingitbythetimethenodeisavailabletothecustomer,
andtheassumedaverageutilizationoftheAIaccelerators.30
• Data ingress/egress: Data into and out of the cluster is metered and sometimes billed
(Google Cloud, 2024a; Microsoft Azure, 2024b; Pal et al., 2021). The communication
ofnodeswithintheclustertoendpointsoutsidethecluster,aswellastheamountofdata
transferredandtimewhencommunicationoccurs,caninformwhethernodesoutsidethe
clusterparticipatedinatrainingrunordeployment.
The exact procedures to allocate, measure, and invoice customer usage for billing purposes are
notpubliclyavailableforanymajorprovider. However,everyprovidermusthaveinternalcontrol
systemsanddiagnosticstorecordthisinformationaccurately,aswellasstatusreportingandother
telemetrytomaintainthehealthoftheirclusters(suchasthestateofindividualmachinesandnetwork
switches). Whilebillinginformationprovidesawidely-measuredbaselineforcustomercompute
usage,intra-clusternetworkinformationsuchasthenetworktopologycanprovidegreaterdetail.
Specifically,knowledgeofwhethertwonodesarecapableofcommunicatingwithinaclusterinforms
whethertheymayparticipateinrunningthesameparallelworkload.
Theoreticalcompute,whilerelativelysimpletocalculateinmostcases,isusefulprimarilytoestablish
anupperlimitonthetotalcomputebudgetofacustomer. Tomapcomputeusageontoaparticular
workload requires additional information at the cluster or node level, as previously covered in
Section3.3.2.
Measuringempiricalcomputebudget—Measurementsofempiricalcomputeusageinvolveobser-
vationsofacluster’shardware-levelcharacteristics,oftenmeasurementsofthenodeitself(perhaps
fromahypervisororotherprivilegedsoftware)orinter-nodecommunicationfabric. Empiricalcom-
pute,incontrasttotheoretical,canprovideahighlypreciseandaccurateaccountingoftheamount
ofcompute,thoughsomelimitationsexist. Weconsiderthattwocategoriesofmeasuringempirical
compute exist: operations and data transfer. Operations refers to the mathematical calculations
performedaspartofaworkload(mostfrequentlymultiplicationandadditionforcontemporaryAI
workloads). Datatransferreferstothemovementofthedatanecessarytoperformthosecalculations:
networklinksfromnode-to-node,orchip-to-chipwithinanodeorloadedfromanAIaccelerator’s
memory.
Whilethesepropertiesareessentiallymetadata,computeproviderswouldneedtodetailcollection
andobservationofthiswithintheirtermsofservicewithveryclearguidelinesabouthowthedata
willbecollected,stored,andused. Whilestrictinternalpoliciesarenecessarytoensuretheintegrity
ofsuchmetadata,thiskindofusagepolicywouldlikelynotrequireanysignificantdeviationfrom
existingpoliciesforsensitivecustomerdatahandling,ordeviationfromthekindsofdatathatare
alreadyoftencollected(AWS,2024g;CoreWeave,2022;FluidStack,2022;GoogleCloud,2024c;
LambdaLabs,2022;Microsoft,2024a).
Withinagivennode,opportunitiestomeasureempiricalcomputeinclude:
• OperationsperformedonAIaccelerators: Individualchipscontainperformancecounters
tomeasureinformationsuchasthenumberofinstructionsexecuted(Wikipediacontributors,
2023). Avendortoolmayberequiredtoaccessthisinformation(NVIDIA,2024b).
• Dataflowto/fromAIaccelerator’smemory: Therateatwhichdataiswrittentoorread
fromtheAIaccelerator’smemorycanbeobservedovertime, allowingmeasurementof
throughputandquantity,andcaninformanestimationofthetotalnumberofoperations
performed(NationalEnergyResearchScientificComputing,2024;Williamsetal.,2008).
• Data traffic between accelerators and other nodes: Node-to-node and chip-to-chip
communicationisanindicatorofparticipatinginthesameworkload,eveniftheworkload
itselfcannotbeclassified(Merritt,2023;NVIDIA,2024a;Shoeybietal.,2020).
30“Utilization”inthiscontextreferstotheusageasaproportionofthenode’stheoreticalpeakcomputational
performance.
28

Evenwithoutprivilegedsoftwareaccesstothenode,othermeasurementsofclusteroperationsare
usefultoinformanestimateofempiricalcompute:
• Powerconsumption: Incaseswhereprecisechiputilizationisnotobservable,measure-
mentsofpowerconsumption(ofanodeorindividualAIacceleratorswithinanode)can
help inform an estimate. The amount of power consumed by each node is considerably
higherwhenanode(orevenanindividualAIaccelerator(NVIDIA,2024c))executesa
workloadcomparedtoidle. However,powerconsumptiondoesnotsimplyscalelinearly
withperformance(Pateletal.,2023),thoughspecificcalibrationforadevicemayenableim-
provedestimation. Powerconsumptionwilltypicallybeawayofmeasuringbothoperations
anddatatransfer,asboththeseactivitiesconsumeenergywithinanode.
• Datatrafficbetweennodes: Granularinformationsuchasthenumberofdatasenttoand
fromthenode,thesourceanddestinationofthisdata,andthetimingwithwhichtheyare
sentcaninformhowmultiplenodesarecooperativelyexecutingthesameworkload.
While many of these measurements alone provide limited insight, combining measurements can
provide more insight into the compute usage of a particular workload (Figure 11). Empirical
measurementsformanupperboundforcomputeusage,asnoteveryoperationcanbeknowntohave
contributedtoaworkload.
3.3.4 DetailedWorkloadVerification
ToverifycompliancewithregulationsonthedevelopmentordeploymentoffrontierAIsystems,it
maybeusefulforacomputeprovidertovalidatemorefine-grainedfeaturesofaworkload,suchas
whetheraparticulartrainingdatasetwasused,themodelarchitecture,orwhetheraparticularmodel
evaluationwasrun. Wecallsuchactivities“detailedworkloadverification.” Thisformofverification
differsfromworkloadclassificationinthatitwillalmostalwaysrequireknowingcertainproperties
ofthecodeand/ordatausedbythecustomer.
Oneundesirableformofworkloadverificationwouldsimplyrequirecomputeproviderstohavedirect
accesstocustomercodeanddata.However,thislevelofaccessisnotacceptable,ascomputeproviders
will not access customer data without permission unless required to maintain the health of their
clusterorlegallycompelled(seeAWS(2024b),andothertermsofservicesfromcomputeproviders).
Internalriskmanagementprocesses,suchasauditingaccesstocustomerdatabyemployees,typically
governdetailssuchaswhenaccessoccurred,bywhom,andwhetheritwasauthorized.
However, using privacy-preserving technologies built into data center hardware, it may become
possibleforacomputeprovider,incollaborationwithacustomer,toverifyparticularpropertiesofa
workloadwithoutobservinganyotherinformation—onlytherequiredverificationresultneedsto
beshared(Aarneetal.,2024). Asoneexample,manymodernCPUsandAIaccelerators,suchas
NVIDIA’sH100,anddatacenterCPUsfromAMDandIntel,comeequippedwitha“trustedexecution
environment”(TEE),allowingtheAIaccelerator/CPU’scustomertoasserttheconfidentialityand
integrityofcode/data,whileexposingonlythecode/datatheychooseto,andhavingfullcontrolover
whotheyexposeitto(Figure12). TechniquesthatleverageaTEEinthiswayareoftenknownas
“confidentialcomputing.” Computeprovidersareincreasinglymakingthesefeaturesavailableto
customers(AWS,2024d;Microsoft,2024b;2023).
Using confidential computing techniques, customers may be able to provably verify particular
governance-relevantpropertiesoftheirworkloadstotheircomputeproviderordirectlytoaregulator.
Forexample,acustomermaywishtodemonstratethattheyranaparticularmodelevaluation,obtained
aparticularresultonamodelevaluation,ordid(not)useaparticulardatasetduringtraining.However,
these techniqueshave yetto be fully validated andimplemented in productioncontexts. Several
organizationsareactivelyresearchinganddevelopingsoftwareforusingconfidentialcomputingto
allow privacy-preserving auditing of models (Mithril Security, 2024b; OpenMined, 2023; 2024).
Therehasalsobeensomeworkonexpandingthesetechniquestoallowprivacy-preservingauditing
oftrainingworkloads(e.g.,thedatasetused,orquantityofcomputeconsumed),thoughthisarea
islesswell-explored(Choietal.,2023;MithrilSecurity,2024a).31 Ifregulatoryrequirementson
computeprovidersenduprequiringthemtovalidatemorefine-grainedpropertiesofworkloads,these
31Choietal.(2023)proposeamethodforverifyingtrainingdata,butitrequiressharingofsensitivedatawith
theverifier.Makingtheschemefullyprivacy-preservingisdiscussedbutleftforfutureworkbytheauthors.
29

Attester Verifier
Device Evidence 4.
1. A device-specific Public and Private key
pair are created on the device, ideally using
a dedicated Security Module. The public
key is shared externally. Security Module
Public key Public key
2. Measurements (e.g. the specific firmware Private key 1. Used to
loaded onto the device) are collected, validate
ideally using a TEE. Using a TEE means signature
measurements are only observable and Signature of 3. Signature of
shareable by the Attester. measurements measurements
3. The Security Module uses the Private key
Used to
to create a “signature” of measurements
authenticate
taken from the device. This will be used to Application

measurements
prove that the measurements collected Processor
came from the device.
TEE
4. Using the evidence provided by the Measurements 2. Measurements
Attester, the Verifier can now validate that
the measurements are genuine.
Figure12: Usingconfidentialcomputingtechniquesallowsan“attester”(customer)tosharehigh-
levelinformationaboutaworkloadwitha“verifier”(e.g.,acomputeprovideroraregulator)such
thattheverifiercantrusttheinformation,withouttheattestersharinganyadditionalcodeordata.
(AdaptedfromAarneetal.(2024).)
kindsofmethodscouldbeusedtoachievethisinawaythatpreservescustomerconfidentialityand
privacy. Inthemeanwhile,weencouragecomputeprovidersanddeveloperstoexploreanddevelop
thesetechniquestoensuretheycanbeimplementedwithoutmeaningfulperformancepenalties,and
whilepreservingotheraspectsofcustomerexperienceandconfidentiality.
4 ConstructinganOversightScheme
Incorporatingrolesforcomputeprovidersinsecurity,recordkeeping,verification,andenforcement,
accompaniedbyappropriatereporting,couldformthebasisofaneffectivecomputeoversightscheme.
SuchaschemecouldenablegreatervisibilityofAIdevelopmentandhelpensuretheadoptionof
appropriatesafeguards. Thereisanopportunitytobuildonandcomplementexistingpoliciesaround
computegovernanceoccurringaroundtheglobe.
ThissectionlooksattheUSasacasestudy. WeexaminetheBidenAdministration’s2023Executive
Order14110onSafe,Secure,andTrustworthyAI(“theAIExecutiveOrder”)(TheWhiteHouse,
2023b): outliningthewaysinwhichitprogressesrecordkeepingrequirementsforforeigncustomers
and signals a need for greater verification and enforcement capabilities. We then explore what
additionalstepsmightberequiredtoenlistcomputeprovidersinadministeringamorecomprehensive
computeoversightscheme,andwherefurtherresearchisneeded. Wehighlighttheimportanceof
internationalizingacomputeoversightscheme,andoutlinesomeofthekeychallengesthatneed
furtherattentionandanalysisbeforethisproposalisreadyforadoption.
UnlikeproposedUSforeigncustomeridentificationrulesforIaaSproviders(FederalRegister,2024),
wefocusonoversightofonlyfrontierAImodeldevelopmentanddeployment,ratherthanallcompute
use. WhileweexploretheseissuesintheUScontext,similaranalysescouldalsobedoneforother
jurisdictions,liketheEU,andintheinternationalcontext. Weencouragefurtherpolicyanalysisin
thisspace.
30

U.S. Department of Commerce
Bureau of Industry National Institute of Standards
and Security (BIS) and Technology (NIST)
Compute
Report provider Report Report large AI models, Sets safeguards
large clusters and supervision violations of security measures, and and regulations
foreign companies regulations evaluation results
Reporting
Compute Domestic AI
Verification
Provider Developer
Assist
enforcement
Enforce relevant
Report large training
controls
runs, IP addresses, etc.
Key
Current proposed regulation
Foreign Customers Proposed additions
Figure2: Additionalmeasures,implementedbytheDepartmentofCommerce,wouldstrengthenthe
intermediaryroleofcomputeprovidersandenableacomputeoversightscheme.
4.1 CaseStudy: ComputeProviders’IntermediaryRoleintheUS
4.1.1 RecordKeepingandReportingintheAIExecutiveOrder
TheAIExecutiveOrderacknowledgestheimportanceofcomputeprovidersinAIregulation,and
begins to impose record keeping and reporting requirements. First, under the authority of the
DefenseProductionAct(DPA),itrequiresfirmsowningordevelopingclusterscapableofcollectively
providing more than 1020 OP/s with more than 100 Gbit/s networking bandwidth32 to report its
existenceandlocation. Onceimplemented,thismeasurewouldprovidetheUSGovernmentwith
visibilityofthemostsignificantcomputeinfrastructureintheUS.Whilethehighreportingthreshold
willnotcaptureallcomputeclusterscapableoftrainingfrontierAI,itwillneverthelessbeusefulin
identifyingrelevantindustrystakeholdersthatwouldplayaroleinfrontierAIgovernance.
Additionally,leveragingthepowersoftheInternationalEmergencyEconomicPowersAct(IEEPA),
theAIExecutiveOrderrequiresthatcomputeprovidersidentifyandreporttotheDepartmentof
CommercewhenaforeignpersonusestheirservicestotrainafrontierAImodel.33 TheDepartment
ofCommercehasproposedrulestoimplementthisthatwouldrequireUScomputeproviders(and
theirforeignresellers)tomaintainCustomerIdentificationPrograms.34
32ThresholdasstipulatedbytheAIExecutiveOrder.Noteitissubjecttoupdates.
33Inthiscase,modelstrainedonwithmorethan1026operationsandoccurringonfrontierinfrastructure.
34TheproposedrulesalsorequireUSIaaSprovidersandtheirforeignresellerstoverifytheidentitiesofall
foreigncustomers. Thisbroadermeasurehascomeundercriticismforbeingineffectiveinaddressingcyber
threats,givingrisetoprivacyissues,andimpactingthecompetitivenessofUScomputeprovision(National
SecurityTelecommunicationsAdvisoryCommittee,2023).Thispaperdoesnotengageinanalysisofthisbroader
measure,andinsteadfocusesonthesubsectionofcomputeforfrontierAI.Asoutlinedintheintroduction,this
narrowerfocusonlycapturesasmallnumberofAIfirmsandcomputeproviders,whichmitigatesmuchofthe
concernaroundregulatoryburden(seediscussioninSection1.4.
31

4.1.2 PotentialforVerificationCapacity
TheAIExecutiveOrderoffersthepotentialforcomputeproviderstoexerciseverificationcapacities.
In a direct sense, the proposed rules would require US compute providers to take a risk-based
approachtoverifyingtheidentitiesofforeigncustomersandtheirbeneficialowners,whetherthe
customer is running a training workload with particular technical properties, and reporting large
trainingrunsbyforeigncustomerstotheDepartmentofCommerce(FederalRegister,2024). In
an indirect sense, the AI Executive Order introduces a range of requirements for AI developers,
whichwilleventuallyrequireverificationcapacitiestobeeffective. Forexample,AIdevelopersare
requiredtoreportonthetrainingoflargemodels,thecybersecurityprotectionstakentosecuremodel
weights,andtheresultsfromred-teamtestingaccordingtoguidelinesdevelopedbytheNational
InstituteofStandardsandTechnology(NIST).WhiletheAIExecutiveOrderdoesnotaddresshow
thesemeasureswillbeverified,computeproviderscouldbecomegovernments’naturalpartnersfor
checkingcompliance.
TheAIExecutiveOrderandtheproposedrulesforIaaSprovidersgivecomputeprovidersarole
inenforcingregulations—enablingtheGovernmenttorequirethecomputeprovidertoprohibitor
limitaccesstoanaccountoranentirejurisdiction—butonlywhenitinvolvesforeigncustomerswith
demonstratedpatternsofusingUSIaaSformaliciouscyber-enabledactivity. Thereiscurrentlyno
explicitauthoritythatrequirescomputeproviderstostopaforeigncustomertrainingafrontiermodel
thatmightbeusedmaliciouslyinthefuture. Theexistingauthoritiesalsowouldnotapplyincases
whererisksarisefrommodelsbeingdevelopeddomestically.
4.1.3 FutureAdditions
The AI Executive Order lays the groundwork for an institutional structure that could support a
computeoversightscheme. Importantly,itbeginstobuildgreaterAIunderstandingandregulatory
capacitywithintheUSgovernment,establishesclearergovernmentaccountabilitiesforfrontierAI
governance,andestablishesfoundationalelementsofabroaderregulatoryframework. Yetitfalls
short of a comprehensive oversight scheme. Additional steps are required to effectively identify
and manage emerging risks and enable proportionate oversight of frontier AI development. We
outline potential measures to achieve this, including ensuring proportionate information security
practices,expandingandstreamliningrecordkeepingrequirements,enhancingverificationroles,and
establishingenforcementcapabilities.
Ensuringproportionateinformationsecuritypractices—Giventhepotentialrisksassociated
withfrontierAI,furtherworkmaybewarrantedtoensurecybersecuritystandardsareproportionate
torisk. BecausecomputeprovidersarecustodiansofsensitivedataandIPforabroadrangeofclients,
actionstheytaketoimprovesecuritywillbenefitalltheirAIdevelopercustomersandtheirrespective
users.35 Further cooperation between industry and government (including bodies like NIST and
CISA)isrequiredtoconsiderwhatcybersecuritystandardsaremostappropriateforentitiesthat
holdsensitivefrontierAI-relatedIP.Thiscouldbeinformedbytheriskprofilesunderpinningthe
cybersecuritystandardsandpracticesthatarecurrentlybeingdevelopedbyleadingAIcompanies,as
pertheirvoluntaryWhiteHousecommitmentstomanageAIrisks(TheWhiteHouse,2023c).
Expandingandstreamliningrecordkeeping—WhiletheproposedrulesrequireUScompute
providerstokeeprecordsonforeignAIdevelopers,significantAI-relatedrisksmayalsoarisefrom
domesticAIdevelopment. Thismaymakeitappropriatetoexpandtheroleofcomputeprovidersto
alsoundertakeKYCondomesticdevelopersoffrontierAItoenableamorecomprehensiveoversight
scheme (Smith, 2023). Under the AI Executive Order, domestic AI developers are themselves
accountableforreportingtheirownfrontiertrainingrunstotheDepartmentofCommerce. Usingthe
computeprovidertocollectinformationthatcouldthenbeusedtovalidatetheseprocesseswould
helpimprovetheireffectivenessandensurecompliance. Inthisway,KYCcouldbeimplementedas
acohesivescheme,drawingonlessonsfromthefinancialsector(Egan&Heim,2023).
Inadditiontousingtrainingcomputethresholds, othermeasuresshouldbeemployedtocreatea
morepreciserisk-managementsystem. Thecurrent1026operationsthresholdminimizesregulations
on existing systems while capturing next-generation models that may pose significant dual-use
risks. However,below-thresholdcomputecouldalsoberelevantinidentifyingproblematictrends
35Note,however,thatstrongcybersecurityattheinfrastructurelevelaloneisinsufficient.AIfirmswillstill
needtoimplementandmaintainstrongcybersecuritypracticesontheirownsystems(Section3.1).
32

(e.g.,fromentitiesinparticulargeographicregions)andentitiestryingtobreakupworkloadsover
multiplecomputeproviders(Heim&Egan,2023). Furthermore,thethresholdshouldbeconstantly
re-evaluatedasfrontierAIevolvesandalgorithmicinnovationsreducethecostoftrainingpowerful
systemsandifourunderstandingofhowtopredictrisksfromcomputeinparticularsystemsgrows
(Pilzetal.,2024). Onthetrainingside,indicatorsliketrainingdata(similartothebiologicalsequence
datacriterionreferencedintheAIExecutiveOrder),thearchitectureoftheAImodel,ortheway
trainingisconductedcouldallbeusefulproxiesforidentifyingrisklevelsfromnewAIsystems.
Onthedeploymentside,whichdoesnotcurrentlyfallunderthepurviewoftheAIExecutiveOrder,
factorsliketheuseofcustomerdata(e.g.,voiceorimages),thescaleofdeployment,thelevelof
accesstotheoutsideworld(e.g.,viatheinternetorphysicaleffectors),andtheabilitytoactwith
limiteddirectsupervisioncouldbeusedtosetarangeofregulatorythresholds(Shavitetal.,2023).
Developingmorenuancedthresholds,beyondbluntcomputecapacityandusage,willrequirefurther
researchandcollaborationbetweengovernment,computeproviders,AIdevelopers,andbroadercivil
society.
Enhancingverificationroles—Thereisanopportunitytoleveragecomputeproviders’verification
capabilitiestohelpensurebothforeignanddomesticAIdevelopersarecomplyingwithAIsafety
standards and requirements. The AI Executive Order requires AI developers to report the total
amountoftrainingcomputeandwhetherbiologicalsequencedatawasusedtotraintheirfrontier
models, as well as the outcomes of safety testing. However, there are presently no verification
methods specified for these requirements. The ability of compute providers to capture insights
fromthemetricsdescribedinSection3couldenableverificationtobeperformedwhileminimizing
privacytradeoffs. Forexample, ratherthanreportingallmetricstotheUSgovernment, compute
providers could instead only report when they have reasonable grounds to suspect a violation of
regulations or standards has occurred. Verification mechanisms will need to be resilient against
evasionandexploitation. Forexample,privacy-preservinginformationsharingbetweencompute
providerscouldbeusedtohelpidentifyandmanageattemptstobreaktrainingrunsdownintosmaller
segments, ortoobfuscatecomputeutilizationpatterns. Asregulatoryframeworksdevelop, there
maybeanopportunityforcomputeproviderstoplayaroleinadvancingbothresponsibletraining
requirementsforfrontiermodeldevelopers,includingnotificationanduseofsecureinfrastructure,
andpre-deploymentsafeguards,forexamplebyrequiringfrontiermodelproviderstodemonstrate
theyhavegovernmentapprovalspriortoplacingamodelonthemarket. Suchapprovalscouldbe
madecontingentontheevaluationofhighlycapablemodelstoaspecifiedstandard(O’Brienetal.,
2023).
Privacy protections could also be aided by the application of confidential computing standards,
whichtechnicallylimittheabilityofcomputeprovidersto‘lookin’atsensitivedata(IBM,2024;
OpenMined, 2023). Further work is required to explore the possibilities of data verification in a
privacy-preservingway,particularlymechanismstoidentifywhenadeveloperisusingbiological
sequencedata.
Establishingenforcementcapabilities—Toeffectivelyleveragecomputeprovidersinaninter-
mediaryenforcementrole,theUSgovernmentwouldneedtoimplementadditionalauthoritiesand
requirementsforthemtoeffectivelyhalttrainingrunsordeploymentinresponsetoviolationsof
set controls and safety standards. Such authority could be linked to a comprehensive regulatory
schemewithcomponentssuchasdeveloperlicenses,trainingriskassessments,pre-deploymentrisk
assessments,andthemonitoringofcriminalactivitythroughmodelsafterdeployment(Anderljung
etal.,2023a),supplementedbyaprocessforappealandcorrectiveaction. Todrawparallelsfrom
otherindustries,financialandaerospaceregulatorsusearangeoffactors,likecustomerriskprofiles,
trackrecords,andcompanypractices,toevaluatethelevelofoversightnecessary. AIdevelopers
withapatternofriskybehaviormaywarrantstricteroversightinordertopurchasecomputingpower.
TheabilitytodeployanAImodelatalargescalemayalsobelinkedtomodellicensingandproper
privacyandsafetyprecautionsonthepartofthecomputecustomerinthefuture.
Onceappropriateauthoritieshavebeenestablished,thereareseveralwayscomputeproviderscould
helpenforcerules. Itcouldbedesirabletobeabletopreventorpauserunsifthetotalamountof
compute used exceeds the limit permitted by present approvals, if deployed models are actively
causingharm,orifthedeveloperisontheEntityList. Computeprovidersalreadyhavetheabilityto
rationorcutoffcomputeaccesstotheircustomers. Therefore,keyworkthatwillneedtobedone
hereincludes:
33

1. establishing formal rules for when AI developers can and cannot access compute at a
particularscale,
2. creatingformalchannelsofcommunicationbetweencomputeprovidersandregulators,and
3. clearlyestablishingrespectiverolesandauthoritiesbetweengovernmentandindustry.
4.2 RegulatingtheComputeProvidersThemselves
ForcomputeproviderstoeffectivelycontributetoAIregulationdownstream,theythemselvesalso
needtobesubjecttoappropriateoversightandcompliancemeasures. Theyarebothintermediaries
andagents: theyactaspass-throughsthatoffercomputingpower(intheformofhardware,often
acquiredfromotherfirms)toAIdevelopers,andtheymakeautonomouschoicesonpricing,select
customers,andprovidedifferentiatedservices.
The AI Executive Order requires that compute providers declare the existence and location of
large-scale compute clusters, and the total amount of computing power available in each cluster.
Ad hoc investigations and spot checks would help ensure compute providers are incentivized to
prioritize this obligation. A chip registry, where policymakers mandate the reporting of the sale
andtransferofcutting-edgeAIchips,couldalsohelpensurecompliance(Fistetal.,2023;Fist&
Grunewald,2023;Sastryetal.,2024). Buttheneedtoverifycomputeprovidercompliancewould
besignificantlyheightenedshouldtheytakeupthekeyroleofscreeningAIdevelopers. Ongoing
training and government and industry engagement could help ensure expectations are clear and
requirementsaremetinawaythatminimizesregulatoryburden. Additionalgovernmentcapacity
would likely be required to ensure appropriate spot checks and investigations can be carried out.
Tohelpensurecomputeprovidersplayanappropriateroleinprovidingsecureinfrastructureand
advancing verification and enforcement, there may also be a role for the licensing of compute
providersthemselves,similartothewayinwhichoperatorsofcriticalinfrastructurearelicensedin
otherdomains(AustralianDITRDCA,2024;CaliforniaEnergyCommission,2024;OFWAT,2024).
Ensuringthatgovernment-establishedregulationsareupheldandnottamperedwithwillbekey.
In cases where the compute provider and AI developer are the same firm or linked by a close
partnership,additionalstepsshouldbeconsidered.Thesearrangementsarecommonformanyleading
AIcompanies,whicheitherbuildAIdatacentersfortheirownproducts,forexample,Google,or
maintainclosefinancialtieswiththeircomputeproviders,likeOpenAIwithMicrosoftandAnthropic
withAmazon. Thestrengthofthesetieshaspromptedrecentantitrustconcerns: inJanuary2024,
theUSFederalTradeCommissionbegananinquiryintothesepartnerships(Ward&Hu,2024). In
suchcases,thereareunusuallystrongincentivestocolludeonfalsereporting,asrapidprogressinAI
developmentisinbothentities’financialinterests. Thiswarrantsadditionalexternalscrutinyand
reporting. Awhistleblowerschemecouldassistinidentifyingandaddressingnoncompliance,butin
thelongerterm,prudentialregulationsmaybeneededtocreateanaccountablecomputeecosystem
and ensure that providers are fit for acting as regulatory pass-throughs. Compliance with these
regulationscouldbelinkedtomaintainingoperatinglicensesoraccessingcutting-edgeAIchips.
Theserulesshouldensuresufficientindependencebetweencomputeprovidersandtheircustomers,
andthatadvancedAIandcomputecapabilitiesaresafeguardedandaccessedinanequitablemanner.
Stepstolimitthepartnershipsthatcreatethestrongestincentivesforcollusion,includingviaantitrust
law,couldalsohelpensureproperoversight.Inmanyindustries,therearerestrictionsonhowplatform
providersmayoperateontheirownplatforms,assuchoperationscaninvolveanti-competitivemarket
practices;asimilarapproachmaymitigateunfairpracticesinthecloudcomputingmarket.
4.3 DomesticGovernmentCapacity
GiventhestrongpublicinterestinmanagingtherisksoffrontierAI,arobustgovernmentinvolvement
willbekeytothesuccessofanoversightscheme(Anderljungetal.,2023a). Buildingonexisting
efforts,theUScouldestablishacentralizedauthoritywithintheDepartmentofCommerceresponsible
forAIriskmanagementandengagementwithcomputeprovidersandAIdevelopers. Locatingboth
industryopportunityandriskmanagementwithinthesamedepartment,alongsideotherAI-relevant
agencieslikeNIST,willhelpenableaholistic,proportionateapproachtofrontierAIcontrols. It
couldalsosupportalignmentwiththeDepartment’sBureauofIndustryandSecurity’s(BIS)work
oncomputehardwarecontrols,whichleverageschannelsofengagementwithsimilarstakeholders.
34

Thisauthorityshouldworkcloselywithindustry,researchers,andothergovernmentstakeholdersto
ensureaholisticapproachtoAIgovernance.
Additionalregulatoryandlegislativeauthoritywilllikelyberequired. TheIEEPAprovidestheUS
governmentwithbroadabilitiestocontroltransactionswithforeignpersonsincircumstanceswhere
thePresidentdeclaresaNationalEmergency(CongressionalResearchService,2024). Thiscould
providethepowerforscrutinyandenforcementagainstforeignpersonsaccessingUScompute,but
therequirementtomaintainaconstantstateof‘nationalemergency’fortheserulestoapplycouldbe
criticizedasgovernmentoverreach(Boyle&Lau,2021). Thegovernmentisalsolimitedinitsability
toeffectivelyutilizecomputeprovidersasanodefordomesticoversight. WhiletheDPAallowsthe
governmenttorequireinformationfromcompaniestoundergoindustrialbaseassessments,thisfalls
shortofestablishingongoingchannelsofinformationsharingandverification,andtherearecurrently
noclearmechanismsforcheckingcompliance. Thedevelopmentofnewlegislationshouldinvolve
thoroughconsultationwithindustryandaffectedstakeholders,aswellasinternationalcounterparts.
4.4 InternationalCoordination
Aharmonizedinternationalapproachwillbeessentialforthesuccessofacomprehensivecompute
oversightscheme: bothtomanagecomplexcross-jurisdictionaloversightandprivacyissues,andto
minimizetherisksofcustomersandbusinessesrelocatingtootherjurisdictionstoavoidregulations.
Internationalstandardsthatpreserveprivacyandconfidentialityshouldbeexploredaskeycomponents
ofthesolution.
Cross-jurisdictionaloversightissues—Existingcross-jurisdictionaldata,privacy,andoversight
issuesassociatedwithcomputeproviderswithaglobalpresencewillbeamplifiedinthecontextofAI
computeoversight. Manylargecomputeprovidersemploygloballydistributeddatacenterstoenable
low-latencyinternationalserviceprovisionandresiliencetolocaldisruptions. Forexample,while
headquarteredintheUS,majorcomputeproviderslikeMicrosoftandAWShavedatacentersspread
across many regions and jurisdictions (AWS, 2024c). However, this distributed architecture can
resultincontradictorylocalanddomiciledregulatoryrequirements. Thishasbeenevidentinthelaw
enforcementcontext,withtheUSenactingtheClarifyingLawfulOverseasUseofData(CLOUD)
Actin2018inresponsetoimpositionsonitsabilitytoaccessdatafromUScomputeproviderswhen
thatdatawasstoredinaforeigndatacenter(Rep.Collins,2018).
In the context of AI compute providers, cross-jurisdictional oversight is of particular sensitivity,
duetoboththecommercialvalueoffrontierAImodelweights,aswellasthestrategicsignificance
of AI. With both the US and China actively competing to be the world leader in AI (The White
House, 2023b), there would be strong incentives for states to misuse any access they may attain
throughacomputeprovideroversightregime. Forexample,China’s2017NationalIntelligenceLaw
stipulatesthatPRCcitizensandcorporationsmustassistwithChina’snationalintelligenceefforts,
if directed (China Law Translate, 2017), and in 2022, the US government used its powers under
the Foreign Intelligence Surveillance Act to order Microsoft to give it access to between 42,000
and43,996accounts(Microsoft,2022). Thiscreatesalow-trustenvironmentthatcoulddiminish
the competitiveness of compute providers in countries that have oversight regimes and diminish
internationalsupportforsuchascheme.
Privacy-preservingstandards—TosupportinternationalcooperationonmutuallybeneficialAI
safetyoversight,computeproviderscouldplayaleadingroleinworkingwithgovernmentstoestablish
privacy-protectingcomputeprovisionnormsandstandards. Theneedtobalanceprivateinterests
withstateinterests,andsecuritywithprivacy,isnotnew. In2017,Microsoftproposedmakingmajor
technologycompaniesakintoa‘DigitalSwitzerland’–refusingtosidewithgovernmentsinany
cyberattackandinsteadupholdinganeutralandtrustedenvironment(Smith,2017). However,in
2022,majortechnologycompaniestookanactivestanceinresponsetoRussia’sinvasionofUkraine:
MicrosoftplayedanactiveroleindefendingUkrainiangovernmentsystemsandnetworks(Farrell&
Newman,2023)andSpaceXimmediatelyprovidedUkrainewithfreeaccesstoitsStarlinksatellite
networks(Jonesetal.,2023). Thishasdemonstratedagrowingwillingnessofprivatetechnology
companiestoplayanactiveroleingeopoliticsandthisshiftshowcasesthelimitationsofvoluntary
rulesandnorms(Farrell&Newman,2023). Inthisenvironment,technicalsolutionscouldbekeyto
establishingthetrustandreliabilitynecessaryforcustomerstotrustinternationally-ownedcompute
providersinthecontextofanoversightscheme. Inparticular,confidentialcomputingtechniques
35

(ConfidentialComputingConsortium,2022)couldensurecomputeproviderscannotbecompelledby
governmentstohandoversensitivedata(Section3.3.4).
Notwithstandingprivacy-preservingstandardstoprotectsensitivecustomerdata,requirementsfor
computeproviderstoreportoncustomersinforeignjurisdictionswillraisesignificantinterjurisdic-
tionalprivacychallenges. EvenbetweenclosepartnersliketheUSandEU,privacyprotectionshave
alreadycomeintoconflictwithfreedataflowsacrossjurisdictions. Forexample,theEU-USPrivacy
Shield (European Commission, 2016) and its predecessor, the International Safe Harbor Privacy
Principles(EUAgencyforCybersecurity,2000),designedtoallowdatasharingbetweentheEUand
US,werebothoverturnedbytheEuropeanCourtofJusticebecauseoftheirfailuretoappropriately
upholdEUcitizens’privacyrights(BBC,2020). Theirreplacement,the2022EU-USDataPrivacy
Agreement,isalsounderscrutiny,withprivacygroupsannouncingtheirintentiontocontestitin
court(Kim,2023). UnilateralUSactiontorequirereportingonforeigncomputecustomerswilllikely
evokesimilarprivacychallengesthatcouldinhibitUScomputeproviders’abilitiestoserveglobal
customers. Tomanageprivacyissueswithcloseallies,theUScoulddeveloptailoredagreementsthat
enableitsoversightrequirementstobemetthroughcomputeprovidersreportingtothegovernment
ofthealliedcountrywithinwhichtheircustomerisdomiciled. Thiscouldbemadecontingenton
somelevelofinformationexchangebetweentheUSandpartnergovernment. Itcouldalsoserve
toincentivizeuptakeofaconsistentschemeamongstlike-mindedcountries. Weencouragefurther
researchtoexploretheseissuesinmoredepth.Ultimately,tobesuccessful,acomprehensivecompute
oversightschemewillneedtoincorporateandgainamultilateralagreementforprivacyprotections
thatbalanceprivacyandnationalsecurity.
Consistentinternationalapproaches—Unilateralactionbyanyonecountry—eventhosewitha
significantIaaSmarketshareliketheUS—alsorisksincentivizingcomputeprovidersandcustomers
toshifttolowerregulatoryenvironments. Thiscoulderodethemarketshareofjurisdictionswith
greateroversight,diminishingtheabilityofgovernmentstooverseeandaddressemergingrisks(Egan
&Heim,2023). Thealreadybroadgeographicspreadofmajorcomputeproviders’datacenters,and
theabilitytoaccessthemremotely,couldpotentiallyenabletheglobalcomputemarkettobemore
easilyrestructured. Unilateralactionwouldalsopushmaliciousactorsandhigh-riskprojectsinto
jurisdictionswithlowerscrutiny,therebyunderminingeffortstoincreaseAIsafety. Achievingthe
greatestconsistencypossibleacrossinternationaljurisdictionswillbekeytoensuringthateffortsto
increaseoversightareeffectiveandrobusttoevasion.
Ultimately,giventheglobalnatureofthecomputeindustry,someformofinternationalagreement
will be needed for monitoring and verification frameworks to be durable. International compute
oversightcoordinationcouldbedevelopedinasimilarformtotheFinancialActionTaskForce,which
currently works to achieve international consistency in the application of anti-money laundering
and counter-terrorism financing (AML/CTF) safeguards and regulations (Financial Action Task
Force,2024b). Asimilarbodyforcomputeoversightcouldfacilitateinformationsharingandhelp
align regulatory approaches and enforcement between international jurisdictions (Egan & Heim,
2023). Yet, while a majority of jurisdictions have strong shared incentives to combat organized
crimeandterrorismfinancing,thereisariskofdifferingincentivesinthecomputeoversightcontext.
Somestates,particularlythoseskepticalofAI-relatedrisks,mayactivelypromotelowerregulatory
environmentsinanattempttoattracteconomicactivityandinvestment–similartohowIrelandhas
usedlowcorporatetaxratestosuccessfullyattractmultinationalcorporationstobedomiciledthere
(Alderman,2021). InitiativesseekingtobuildasharedunderstandingofAI-relatedrisks,likethe
2023UKSafetySummit(UKGovernment,2024),willcontinuetobeimportantforstrengthening
alignmentoncomputeissues. Manycountries,forexample,India,UK,andJapan,arealsoexploring
options to build greater sovereign compute capacity (Government of India, 2023; Nagao, 2023;
UKResearchandInnovation,2023). Thisincreasingself-reliancecouldlowerinterestincommon
internationalapproachesthatmightimpactnationalgoals. Ensuringinternationalbuy-intoacompute
oversight scheme would therefore require substantial diplomatic engagement alongside broader
economicincentives.
Internationalcomputeoversightcouldbeadvancedthrougha“clubapproach”(Trageretal.,2023)
thatpredicatesaccesstocutting-edgechipsonadherencetothescheme.AstheUS,inpartnershipwith
itsallies,currentlyhasachokeholdonthemanufacturingoftheadvancedchipsneededforfrontierAI
compute(Allenetal.,2023),itcouldrestrictexportstojurisdictionsthatareunwillingtoimplement
appropriateoversightmeasures. JustasunimpededaccesstotheUSbankingsystemisconditioned
on a jurisdiction’s compliance with FATF standards and regulations (Farrell & Newman, 2023;
36

FinancialActionTaskForce,2024a),sotoocouldaccesstoadvancedAIchipsrequireadherence
withestablishedcomputeoversightstandards(Sastryetal.,2024). Therewouldbesignificantrisks
withthisapproachthatrequirefurtheranalysis. Forexample,theclubapproachcouldsignificantly
impacttheUSsemiconductorindustryanddiminishUStechnologyleadership. Itssuccessisalso
predicated on the US and aligned partners maintaining the lead in advanced chip hardware. But
ifcarefullyimplementedwithenoughinternationalconsultationandengagement,itcouldprovide
incentivesforabroaderrangeofcountriestooptintothescheme.
Eveninthecontextofnarroweroversightclubs, thereisabenefitinsupportingglobalstandards
onhowcomputeprovidergovernanceingeneralcansupportAIoversightandregulation. Akey
challengewillbesupportingcooperationbetweengeostrategicrivalsliketheUSandChina,asthe
strategicsignificanceanddual-usecapabilitiesofAIincentivizestrongcompetition. However,the
foundationforincreasedcooperationisalreadybeingestablished: boththeUSandChinaattended
the2023AISafetySummitandsignedtheBletchleyDeclarationforeshadowinggreatercooperation
onsafetyissues(PrimeMinister’sOfficeetal.,2023),andtheUSandChinahavealsobilaterally
agreedtoworktogetheronmitigatingAIsafetyrisks(Murgia,2024).
InternationalcooperationcouldbefurtherstrengthenedbycenteringcomputegovernanceissuesinG7
andG20discussions–bringingtogethermajoreconomicplayerstoagreeuponsharedprioritiesinthis
spaceandbuildingonexistingagreementstocooperateonAIgovernance(TheWhiteHouse,2023d).
EngagementwithlargeregionalbodiesliketheIndo-PacificEconomicForum,theAssociationof
SoutheastAsianNations(ASEAN),andtheAfricaUnion(AU),couldencouragebuy-inforcompute
oversightharmonization. Workingwithglobalandregionalbanksmayalsohelpunlockoptionsto
linkinvolvementwithfundingandinvestment.
The details of an international harmonization scheme require further research, consultation, and
analysis. Further work is needed on issues of verification and enforcement between countries.
Nevertheless,weencouragepolicymakerstogivegreaterconsiderationtotheneedforcooperative
computeprovidergovernanceininternationaldiscussions,asafirststepinworkingtowardamutually
beneficialscheme.
5 KeyChallenges
Whilecertaintechnicalandinstitutionalcapabilitiesforconductinginfrastructuregovernancealready
exist and could be employed, many areas still require further research to ensure robustness and
scalability. Furthermore, as compute becomes an increasingly important resource in the global
economy,regulatorswillneedtomakesurethataccesstocomputeisequitable,competitive,and
privacy-andconfidentiality-protected. Regulationalsoneedstostriketherightbalancewithpublic
safetyasAIcapabilitiesdevelop,ideallywithdifferentiatedregulatoryleversthatenablespecificand
nuancedpolicies. Below,wepresentsomekeytechnicalandgovernancechallengesthatshouldbe
exploredinthenearterm. Thegeneralchallengesandconsiderationsofusingcomputeasapolicy
leverarediscussedinSastryetal.(2024)andareapplicablehere.
5.1 TechnicalChallenges
Variationinworkloadsignaturesduetochangesinalgorithmsandhardwareatthefrontier.
Certainsignatures(e.g.,networkbandwidthutilization,AIacceleratorcoreutilization)couldbeused
toclassifycustomerworkloads. However,thesesignaturesdependonthemodelarchitectureand
trainingalgorithmusedtotrainfrontiermodels,whichwilllikelychangeovertime(Rabinovitsj,
2023).36 Additionally,algorithmicprogresswithinonetypeofmodel(e.g.,utilizingAIaccelerators
moreefficiently)wouldalsochangeaspectsofthissignature. Inordertoensurethatinfrastructure
governancemeasuresareeffective,regulatorsandcomputeprovidersneedtobekeptawareofhowthe
state-of-the-artalgorithmsandhardwarearechanging;classificationtechniquesneedtobeupdated
overtimetotracktheseadvancements.
Methodsforworkloadclassificationthatarerobusttoadversarialgaming.
Inadditiontothisnaturalvariationinworkloadsignatures,adversarialactorsmayattempttocircum-
36Forexample,techniquestoreducethememoryfootprintoftrainingareanactiveareaofresearch(e.g.,
(Dettmersetal.,2022)).
37

ventdetectionbyintentionallychangingthecomputationalpattern37 oftheirworkload.38 Compute
providerswillhavetodevelopclassificationmethodsthatarerobusttodeliberateobfuscationand
adoptred-teamingtechniquestocheckagainsttheseattacks. Thesechangescouldbemuchsmaller
andmoreunpredictablethanthenaturalvariationofalgorithms,sothesegamingtechniquesneedto
beanticipatedpriortodeployingtheclassificationscheme.
Preventing evasion by structuring training runs across multiple data centers or compute
providers.
Aswithmoneylaunderingtechniquesobservedinthefinancialindustry,maliciouscustomersmay
split their workloads (e.g., training runs) across multiple data centers or compute providers to
evaderegulations(apracticedescribedas“structuring”inthefinanceindustry(SanctionScanner,
2024)). Regulatorsandcomputeproviderswillhavetodevelopandconstantlyupdatetechnicaland
governancemethodstopreventevasion. Overtime,techniquesforavoidingdetectionwillevolve,as
willmoresophisticatedapproachestodetection. Thisshouldbecomeanactiveandresourcedareaof
technicalgovernanceresearch.
Detectingtrainingrunsdistributedacrossthedatacentersofasingleproviderisrelativelystraight-
forwardduetotheprovider’sconsolidatedinsightintoinfrastructureandrelevantcustomermetrics.
However,whenworkloadsaredistributedacrossmultipleproviders,computeprovidersfacesignifi-
cantchallengesinconsolidatingdataforanalysis. Yet,inpractice,thenumberofproviderscapable
ofdeliveringtherequisitelevelofcomputeforhigh-riskmodelsislimited(Richter,2024). This
issuecanbeaddressedbyatechnicalframeworkthatfacilitatesthesecureandprivacy-preserving
informationexchangebetweencomputeproviders—beingmindfulofthecommercialsensitivities
andpotentialantitrustimplicationsassociatedwithsharingdetailsabouttrainingrunsandotherclient
data.
Moreover,thestrategicimplementationofacomputethreshold(Pistilloetal.,forthcoming)could
serveasadeterrentagainst“structuredtraining”practices. Next-generationAImodelsgenerally
necessitateanorderofmagnitudemoretrainingcomputethantheirpredecessorstoachievemean-
ingfuladvancementsinperformance.39 Acomputethresholdsetslightlyabovethecurrentmodels,
forexample,theoneusedintheAIExecutiveOrder,reflectstherealitythatfuture,moreadvanced
modelswillnotjustrequiremarginalincrementalcomputeincreasesbutratheranexponentialscale-
up(usuallyanorderofmagnitude). Practically,thisleadstothenecessityofinvolvingmorethan
ten compute providers to distribute the workload sufficiently to circumvent the threshold. This
requirementimposessubstantiallogisticalandperformancechallenges. Simplyidentifyingmore
thantencomputeproviderswithsufficientcomputecapacityoverwhichtostructureaworkloadis
aformidablechallenge,anddoingsowithoutdetectionisevenmoredifficult. Furthermore,next-
generationmodels—giventheexponentialincreaseintrainingcompute—increasethechallenges
even further. Should the exponential scaling of training compute persist, it would necessitate a
proportionallyexponentialincreaseinthenumberofcomputeprovidersinvolved,exacerbatingthe
challengesevenfurther.
Usingprivacy-preservingtechnologiesfordetailedworkloadverification.
Emergingprivacyandverificationmechanismssuchastrustedexecutionenvironmentsandproof-
of-training may allow multiple parties to cooperate without the risk of exposing confidential or
sensitiveinformationtoeachother. Forexample,acomputeprovider,dataprovider,andsoftware
providercouldcooperateinamutuallybeneficialtrainingrunwithoutneedingtosharetradesecrets
37AcustomermightattempttohidethefactthattheyareengaginginAItrainingbyusingnon-standard
numberrepresentations,affectingtrafficto/fromoutsidenetworks,ordeliberatelyusinglessefficientalgorithms
withdifferentworkloadcharacteristics,suchasunder-utilizingmemoryorcomputation.However,themorea
customerattemptstodisguiseworkloadsinthisfashion,thegreaterthecostintermsoflostefficiency.Inthe
contextoffrontiermodeltraining,whereasingleworkloadcancosttensofmillionsofdollars,perhapsthese
lossescouldbesignificantenoughtomakemanyformsofobfuscationtoocostly.
38Intheeventofadversarialactorsattemptingtoobscuretheiractivities,itshouldbenotedthatsuchgaming
ofthesystemtypicallycomesatacost,potentiallyaffectingtheefficiencyorperformanceoftheAIsystem
beingtrained.Computeprovidersandregulatorswillneedtoconsiderwhetherthepenaltiesfornon-compliance
aresubstantialenoughtodetersuchbehavior, weighingifthecostofcircumventingoutweighsthecostof
compliance.
39Scalinglawssuggestthatachievingsubstantialenhancementsinperformanceondownstreamtasksneces-
sitatesexponentialincreasesintrainingcompute. Thisprincipleunderscoresthatcomputeinvestmentsgrow
exponentiallyforcomparativelylinearimprovementsintaskperformance(Owen,2024).
38

orpersonallyidentifiableinformation,producingatamper-evidentandprivacy-preservingtraining
recordthatcanbelaterscrutinizedbyaverifier. Moreworkisneededinthisareatodeveloprobust
hardwaremechanismsandalgorithmictechniquesthatcanprovablyaccountforandverifyaspectsof
computeusage. Anymethodsofde-identifyingpersonalorconfidentialdataforsuchexercisesmust
berobustenoughtomeetthestandardsimposedbykeyprivacylaws,suchastheEUGDPR,toavoid
personaldatabreachesorprivacyconflicts.
Creatingarobustcustomeridentificationscheme.
Work must be done to robustly link cloud accounts to particular individuals and entities. This is
neededforkeyfunctionslikeliabilitytracing,developerlicensing,exportcontrolenforcement,and
defendingagainst“structured”trainingrunswhereanadversarialactordistributesitsworkloadacross
multiplecomputeproviders. Furthermore,advancesinAImaycontinuetoincreasethechallengeof
verifyingcustomers’identities. Forexample,websitesarealreadyclaimingtouseneuralnetworks
togeneratephotosofhighlyplausiblefakeIDs,(Cox,2024)whichcouldpotentiallybeappliedto
generate fake business documentation.40 This issue is not unique to compute provider oversight
andwouldneedtobeaddressedonabroaderscaletoinvestigatehowAIcouldhelpfacilitatefraud,
moneylaundering,andothercriminalactivity.
However, as discussed in Section 1.4, customer identification within the context of frontier AI
predominantlyinvolvesalimitednumberofentities,primarilylarge-scalecorporations. Ratherthan
necessitatingwidespreadidentificationefforts,ourfocusisonconductingthoroughverificationsfor
thisselectgroup,ensuringthatthesein-depthanalysesarebotheffectiveandtargeted.
Challengesfromtechnologicaldevelopments.
Theutilityofcomputeprovidersasintermediaryregulatorsissupportedbytheneedforsignificant
computationalresourcesforthetraininganddeploymentoffrontierAImodels(Sastryetal.,2024).
WhilecurrentcomputeandAItrendsappeartoreinforcetheprimacyoflarge-scalecomputeforsuch
models,avarietyoftechnicaldevelopmentsmaychallengethisnorm(Heim,2024;Pilzetal.,2024;
Sastryetal.,2024). Itwillbeimportanttoensurethatcomputegovernancepolicyiscomplemented
byresearchintoothereffectivemechanismsforAIgovernance.
5.2 GovernanceChallenges
Maintainingequitableaccess.
Increasing regulatory requirements on both compute providers and customers can increase the
barrierstoentry,preventingsmaller,lesswell-resourcedactorsfromenteringthemarket. Thisrisks
intensifyingpowerconcentrationamonghyperscalers. Keychallengesincludemakinglegislation
legible,ensuringthatsecureimplementationmethodsareaccessible,andstrikingabalancebetween
safetyandregulatoryburdensatvariousthreatlevels. Forexample,thetechnicaltoolsneededfor
computeverificationshouldbeaccessibletopotentialproviders. Regulatoryagencies,suchasNIST,
canplayaroleindeterminingstandardsandfacilitatingopen-sourcesolutions.
Strengtheningregulatorystructuresforin-housecompute.
ManyAIdeveloperscurrentlyoperatetheirowndatacentersfortraininganddeployingAIsystems.
Thisprovidesadditionalchallengesforoversight. SincetheAIdeveloperandthecomputeprovider
areessentiallythesameentity,theymaybeincentivizedtocollude,weakeningtheverificationand
enforcementcapabilitiesprovidedbyanindependentcomputeprovider. Insuchcases,prudential
regulations,whistleblowerschemes,orevendirectinspectionsbytheregulatormaybenecessaryto
ensureadequatesupervision. Experiencemaybedrawnfromthefinancialworld,whereregulators
faceasimilarchallengewithcorporationsrunningtheirownbanks(ConsumerFinancialProtection
Bureau,2023). Moreworkshouldbedoneondevelopingbothregulatoryandtechnicaltoolsthat
enablerobustandlow-costoversightinthesesituations.41
Ensuringcompliancewithprivacycommitmentsandrelatedlawsonprivacyanddatatransfer.
Althoughwediscussedprivacy-preservingmethodstoperformcomputeaccountingandworkload
classification, it is critical that any implementation of an infrastructure governance scheme is in
40ThecomplexityofverificationprocessesisfurtherincreasedbythediversityofnationalIDandbusiness
registrationregulationswhenconsideredinaninternationalcontext(e.g.,IndiahasmoreadvancedIDverification
systemsthanothercountries(India’sMinistryofElectronicsandInformationTechnology,2023)).
41E.g.,zero-knowledgeproofsthatregulatorscantrusttoverifycomputeusagewithouthavingdirectaccess
todatacentersorsensitivedata.
39

compliancewithexistingprivacylawsandcommitments(e.g.,thatpersonaldataisnotprocessedfor
purposesbeyondthatforwhichthereexistsasolidlegalbasis). Theremayalsobeissuessurrounding
internationalapplicationforforeignprivacylaw. Forexample,ifUSprovidersarerequiredtocollect
informationoncustomersintheEU,theUSgovernmentislikelytofacesimilarchallengesfrom
EUinstitutions,memberstates,civilsociety,andUScompanieswhohavelongdealtwithEU-US
datatransferlegaluncertaintiescausedbyUSnationalsecuritydatacollectionandSchremslegal
challengesregardingsuchcollectionforthepastdecade. Inthelong-term,therealsoneedstobea
conversationabouthowtobalanceprivacycommitmentswithpublicsafety,differentiatingbetween
AIsystemswithvaryingrisklevels.
Preventingregulatoryflightacrossborders.
Wehaveoutlinedinternationalharmonizationasakeysteptominimizetheriskofcomputeproviders
andAIdevelopersanddeployersrelocatingtheirbusinessesorsimplymovingtheirworkloadsto
jurisdictionswithlowerregulatorystandards. However,furtherworkisneededtoexplorethemost
effectivemechanismsforsupportingbroadbuy-intoacoordinatedregulatoryscheme,aswellas
effectiveapproachesforincentivizingbusinessestoremaininhigher-regulatoryenvironments. This
workwouldbeaidedbyanalysisontheelasticityoftheglobalcomputeandAImarkets,andthe
extenttowhichbusinesseswillattempttoavoidoversightmeasures.
6 Conclusion
AsgovernmentsmovetotakeactiononaddressingAIrisks,computeproviderscanplayakeyrolein
ensuringregulationsareupheldandenforced. TheirconcentratedroleintheAIsupplychainallows
themtouserecordkeeping,verificationandenforcementcapabilitiestohelpsecuresensitiveAI-
relatedIPanddata,engageingreateroversightofemergingAIrisks,providepost-incidentattribution
andforensics,preventbadactorsfromtrainingfrontierAImodels,andensureAIdevelopersadhere
tosetstandards. Inthisway,theyhavetheabilitytoactassecurers,recordkeepers,verifiers,and
enforcers.
Implementingthisregulatorymodelinawaythatpreservesprivacyandenablesinnovationwillbe
key. Ouranalysisindicatesthatselectedmechanismsofthesegovernancecapabilitiesaretechnically
feasibleandpossibletoimplementinaprivacy-preservingway. However,furtherworkisrequiredto
ensuresuchagovernancemodelremainsresilienttoevasionefforts,andtofurtherrefineparticular
technicalmechanismsandstandardsthatpreserveprivacyandinnovationwhileallowingsufficient
oversight. Greateroversightwouldalsoberequiredofthecomputeprovidersthemselves. Thiswill
requireclosecollaborationbetweencomputeproviders,governments,andtheresearchcommunity.
Whenscaledinternationally,thisgovernancemodelhasthepotentialtosupportglobalAIgovernance
architecture. Internationalcoordinationwillbeessentialforaddressingcross-borderoversightand
dataissues,aswellastoreducetheriskofcomputeprovidersandAIdevelopersrelocatingtolower
scrutinyjurisdictions.
Usingcomputeprovidersasintermediaryregulatorswillbemosteffectiveataddressingrisksarising
fromlarge-scaleAItraininganddeployment,ratherthanallAI-relatedrisks. Moreover,theviability
ofcomputeasagovernancenodemaybechallengedbydevelopmentsinhardwareandsoftware,
whichcouldreducetheneedforlarge-scaledatacenterusage(Sastryetal.,2024;Pilzetal.,2024).
Theseproposalsshouldthereforebecomplementedbyotherregulatorymeasuresasrequired.
Computeproviderscanplayakeyroleinagovernanceregimethatprotectsprivacyandinnovation,
while ensuring sufficient oversight to mitigate critical AI-related risks. We urge policymakers,
regulators,computeproviders,andtheresearchcommunitytoworktogetheronthenextsteps.
40

Acknowledgments
Wewouldliketoexpressourthankstothepeoplewhohaveofferedfeedbackandinputontheideasin
thispaper,includingArisRichardson,BoxiWu,ChristianTroncoso,ChristophWinter,Christopher
Hoff, Chris Phenicie, Hadrien Pouget, Haydn Belfield, Keegan McBride, Konstantin Pilz, Maia
Hamin,MarkusAnderljung,MauricioBaker,OwenLarter,PamDixon,PeterCihon,TreyHerr,and
ZaheedKara.
WethankBethEakmanforcopyeditingandJoséMedinaforformattingassistance.
OpenAI’sChatGPTandGoogle’sGeminiAdvancedwereusedforeditingassistancethroughoutthis
paper.
A OverviewofComputeProviderTechnologies
AIcomputinginfrastructureistypicallyprovidedthrough“datacenters”,buildingsdesignedtopower,
house,andoperatelargeamountsofcomputinghardware. AIdatacenterscontainmany“servers,”
computersoptimizedforAIcomputationalworkloads(weabstractlyrefertoserversas“nodes”in
Section 3).42 Each server contains a variable number of CPUs (general-purpose processors), AI
accelerators(specializedAIprocessorssuchasGPUsandTPUs),networkingtoallowthesedevicesto
communicate,andshareddatastorage(Figure13). ArelativelylargenumberofAIaccelerators,and
thecapacityforthosedevicestocommunicateathighspeed,aretheprimaryattributesdifferentiating
AIdatacentersfromotherkindsofdatacenters.
AIacceleratorscontainmany“cores,”sub-processorsthatareoptimizedforsimple,parallelcompu-
tation. AIacceleratorsreachhighthroughputasmeasuredbyoperationsperunittimeduetoboth
thenumberofcoresandthecapabilityofthesecorestoperform“vectorprocessing”: simplemath
operationsonanentirearrayofnumbersinasinglestep. Contemporarydeeplearningworkloadsare
efficientlyimplementedinsoftwareusingmatrixmultiplication,andthevectorprocessinghardware
isanefficientmechanismforcomputingthesematrices. Differenttypesofcoresmayexistwithina
singleAIaccelerator,whereeachtypeisoptimizedforhandlingdifferenttypesofinstructionsor
inputdata,suchasgraphicsandvideogames,ormixed-precisionoperationsbeyondsimpleparallel
operationssuchasmatrixmultiplication.
The primary goal of a compute provider is to map customer requests for compute (in the form
ofworkloadsor“machineinstances”)tophysicalhardwareresourcesefficiently: achievinghigh
utilizationofthe(expensive)hardwarewhilemaintainingsecurityandhighperformance. Toachieve
this,providerstypicallyprovide“virtualization.” Thismeansdynamicallycreatingvirtual(rather
thanphysical)versionsofthehardwarewithinaserver,eachwiththeirownoperatingsystemand
software,andisolatedcodeanddata. Thesevirtualserversareoftenreferredtoas“instances,”and
areusedtopartitionphysicalhardwareresources(e.g.,cores,storage)tobeefficientlysharedacross
separatecomputationalworkloadsanddifferentcustomers.Forthepurposesofthekindsofworkloads
consideredinthispaper(large-scaleAIworkloadsrunondedicatedsingle-tenantinfrastructure),
sharingresourcesacrossworkloadsratherthancustomersismorerelevant. Virtualizationexistsin
parttosubdivideaprovider’sphysicalhardwareresources,butalsoasamechanismtoisolatethe
provider from the customer. In cases where the tenant is the sole tenant of a server, two options
exist: the provider can manage the server in the form of a hypervisor layer to provide services
suchasadditionalsecurity,networkingconfiguration,andsoftwaremanagementthroughanAPI,
ortheprovidercanprovidea“baremetal”instancetothecustomer,inwhichcasethecustomeris
responsibleforallsoftware. Eveninthebaremetalinstance,theprovidermaintainscontrolovertheir
network.
Onthesoftwareside,customercodeisoftenrunincombinationwithorontopofastandardizedset
ofsoftwarepackagessuchasframeworksandAPIsprovidedbytheinfrastructureprovider,setup
bydefaultoneachinstance. Codeforaparticularworkload(e.g.,trainingamodel)isorchestrated
bytheCPU,whichschedulestaskstorunonAIaccelerators. ThemaincodeexecutedonanAI
acceleratoris“computekernels,”smallprogramswrittentoexecuteaspecificcomputationaltask
onacore,typicallyinvolvingoperationsonmatrices. ComputekernelsareoftenprovidedbyAI
42Typicallyanodeandaserverareequivalent,but“server”referstothephysicalhardware,whilea“node”is
aunitofcomputationalresourceswithinthecluster’sinfrastructure.
41

AI Data Center
Server Other
servers
Storage
CPU CPU Shared
networking
Shared
storage
GPU / TPU GPU / TPU
Core Core
Networking
Shared power
and cooling
Instance Instance
Figure13: AlogicaldiagramofthesoftwareandhardwarecomponentsandinteractionsinanAI
datacenter. AuserprovidestheirAIcodeanddata,interactingwithasoftwarestackthatdiffers
dependingonproviderinfrastructurebutinherentlyincludesthehardwareinteractionsdepictedabove.
Aservercanbepartitionedintovirtualinstances,whereeachinstancehasafractionofthephysical
resources: CPU,GPU/TPU,networking,andstorage.
accelerator firms (e.g., NVIDIA’s CUDA library) or generated by a compiler (e.g., Triton), with
supportforcustomerswritingtheirowncustomkernel. AIacceleratorfirmsalsogenerallyprovide
performancemonitoringanddebuggingtools,whichmeasurevariousaspectsofanAIaccelerator’s
performance,suchaswhichcoresareactive,whetherthecoresarerunningatfullcapacity,andthe
amountofdatabeingtransmittedto/fromtheAIaccelerator’smemory. Typicallythesetoolsrelyon
hardware-based“performancecounters,”whichtrackdifferentmetricsontheAIaccelerator.
The infrastructure provider runs management and scheduling software, which accepts customer
requests and issues new instances to the customer, and allocates available hardware resources to
workloadsbasedontheircomputationalrequirements. Intandem,anothersoftwaresystemmonitors
andmaintainsthecluster,trackingmachinehealth(powerconsumption,temperature,networkstatus,
etc),andyetothersoftware. Thismanagementsoftwareallowsinfrastructureproviderstotrackwhich
resourcesarebeingusedbywhichcustomers,andbillcustomersfortheresourcestheyareusing.
B ObservableDataAttributes
42

Table4: Anoverviewofobservabledataattributes.
Involves
| Visible |     |     | Easeof | Easeofcir- |
| ------- | --- | --- | ------ | ---------- |
Uses collectionofdata
| attribute |     |     | implementation | cumvention |
| --------- | --- | --- | -------------- | ---------- |
notalready
widelycollected?
|     | Workloadclassification. |     | Alreadycollectedby |     |
| --- | ----------------------- | --- | ------------------ | --- |
Highly
|               |                          | No,already | computeprovidersto |             |
| ------------- | ------------------------ | ---------- | ------------------ | ----------- |
| Hardware      |                          |            |                    | difficultor |
|               | ThequantityofAI          | collected. | setupandprovision  |             |
| configuration |                          |            |                    | impossible. |
|               | acceleratorsrequestedand |            | infrastructure.    |             |
requestedby
networkingsetuparestrongly
thecustomer
suggestiveoftheworkloadsa
customerintendstorun.
Numberof
| hoursthat | Workloadclassification, |     | Alreadycollectedby | Highly |
| --------- | ----------------------- | --- | ------------------ | ------ |
No,already
resources(e.g., computeaccounting. computeproviders difficultor
collected.
| AIaccelerators) |                          |     | forbillingpurposes. | impossible. |
| --------------- | ------------------------ | --- | ------------------- | ----------- |
| areinuse        | Allowshigh-levelboundary |     |                     |             |
settingonworkloadtype/size.
Possible,but
Workloadclassification,
|     |     |     | Possibletocollect | would |
| --- | --- | --- | ----------------- | ----- |
computeaccounting.
|     |     |     | usingexisting | involve |
| --- | --- | --- | ------------- | ------- |
No,already
Powerdraw Allowshigh-levelboundary tooling.Already substantial
collected.
|     | settingonworkloadtype/size, |     | collectedbysome   | cost       |
| --- | --------------------------- | --- | ----------------- | ---------- |
|     | asincreasedpowerdraw        |     | computeproviders. | efficiency |
|     | correspondstoincreased      |     |                   | penalties. |
throughputforaparticular
device.Powerconsumption
overtimemayallow
differentiationofinference
fromtraining(Pateletal.,
2023).
Possible,but
Workloadclassification,
|     |     |     | Possibletocollect | could |
| --- | --- | --- | ----------------- | ----- |
computeaccounting.
|     |     |     | usingexisting | involve |
| --- | --- | --- | ------------- | ------- |
No,already
| Network   |                          |            | tooling.Already | substantial |
| --------- | ------------------------ | ---------- | --------------- | ----------- |
|           | LargeAItrainingworkloads | collected. |                 |             |
| bandwidth |                          |            | collectedbysome | cost        |
requirehighbandwidth
| betweenAI |     |     | computeproviders. | efficiency |
| --------- | --- | --- | ----------------- | ---------- |
betweenservers.Different
| accelerator |     |     |     | penalties. |
| ----------- | --- | --- | --- | ---------- |
communicationpatterns
servers
correspondtodifferentkinds
ofworkloads,andbandwidth
utilizationisrelatedtothe
quantityofcomputation
performedoneachserver.
Possible,but
|     | Workloadclassification, |     | Possibletocollect | could   |
| --- | ----------------------- | --- | ----------------- | ------- |
|     | computeaccounting.      |     | usingexisting     | involve |
No,already
| Network   |                            |            | tooling.Already | substantial |
| --------- | -------------------------- | ---------- | --------------- | ----------- |
|           | Differentbandwidthpatterns | collected. |                 |             |
| bandwidth |                            |            | collectedbysome | cost        |
correspondtodifferentkinds
| withinAI |     |     | computeproviders. | efficiency |
| -------- | --- | --- | ----------------- | ---------- |
ofworkloads,andbandwidth
| accelerator |                           |     |     | penalties. |
| ----------- | ------------------------- | --- | --- | ---------- |
| servers     | utilizationisrelatedtothe |     |     |            |
quantityofcomputation
performedwithineachserver.
Continuedonnextpage.
43

Table4–Continuedfrompreviouspage.
Involves
| Visible   |      |                  | Easeof         | Easeofcir- |
| --------- | ---- | ---------------- | -------------- | ---------- |
|           | Uses | collectionofdata |                |            |
| attribute |      |                  | implementation | cumvention |
notalready
widelycollected?
Possible,but
|     | Workloadclassification, |     | Possibletocollect | could   |
| --- | ----------------------- | --- | ----------------- | ------- |
|     | computeaccounting.      |     | usingexisting     | involve |
No,already
| AIaccelerator |                           |            | tooling.Difficultto | substantial |
| ------------- | ------------------------- | ---------- | ------------------- | ----------- |
|               | LargeAIworkloadstypically | collected. |                     |             |
| core&memory   |                           |            | collectfor          | cost        |
havehighmemorybandwidth
| bandwidth |     |     | bare-metalservices. | efficiency |
| --------- | --- | --- | ------------------- | ---------- |
utilization,andcore
| utilization |     |     |     | penalties. |
| ----------- | --- | --- | --- | ---------- |
utilizationwilltendtobe
constantfortraining,while
inferenceistypicallyvariable.
Potentially.This
degreeof
telemetryonan
Possible,but
|     | Workloadclassification, | individual |                   |         |
| --- | ----------------------- | ---------- | ----------------- | ------- |
|     |                         |            | Possibletocollect | could   |
|     | computeaccounting.      | customeris |                   |         |
|     |                         |            | usingexisting     | involve |
unusual.Policies
| Performance |                         |                   | tooling.Difficultto | moderate   |
| ----------- | ----------------------- | ----------------- | ------------------- | ---------- |
|             | Lowerprecisioniscommon  | forcollectionand  |                     |            |
| countersby  |                         |                   | collectforbaremetal | cost       |
|             | inAIworkloadsandallows  | analysiswould     |                     |            |
| numerical   |                         |                   | services.           | efficiency |
|             | differentiationfrommost | needtobeclearly   |                     |            |
| precision   |                         |                   |                     | penalties. |
|             | scientificcomputing     | outlinedin        |                     |            |
|             | workloadsandpossibly    | provider’stermsof |                     |            |
|             | gaming.Countersalso     | service.          |                     |            |
provideadirectmeasurement
ofoperationsconsumedbya
workload.
|     | Workloadclassification, |     |     | Difficult: |
| --- | ----------------------- | --- | --- | ---------- |
|     | computeaccounting.      |     |     | training   |
requires
Modeltrainingrequires
|                |                      |             | Notcurrently | modifying |
| -------------- | -------------------- | ----------- | ------------ | --------- |
| Modificationof | changingtheweightsin | Potentially |              |           |
|                |                      |             | possible.    | weightsin |
| weightsin      | memoryusingabackward |             |              |           |
memoryto
| memory | pass.Typicallytheonlylarge |     |     |     |
| ------ | -------------------------- | --- | --- | --- |
behighly
datastructuresinmemoryare
performant.
theweightsandactivations,
soitshouldbepossibleto
observewhetherstoresare
madetothatregionof
memory.Themagnitudeand
frequencyofmemoryupdates
arerelatedtothequantityof
computeconsumed.
Yes.Can
|     |                         | potentiallybe |                   | Unclear |
| --- | ----------------------- | ------------- | ----------------- | ------- |
|     | Workloadclassification, | made          | Possibletocollect | (highly |
Workloadhy- computeaccounting,detailed privacy-preserving withcustomer dependent
perparameters workloadverification. usingconfidential consent. onimple-
|     |     | computing |     | mentation). |
| --- | --- | --------- | --- | ----------- |
techniques.
Continuedonnextpage.
44

Table4–Continuedfrompreviouspage.
Involves
| Visible |     | Easeof | Easeofcir- |
| ------- | --- | ------ | ---------- |
Uses collectionofdata
| attribute |     | implementation | cumvention |
| --------- | --- | -------------- | ---------- |
notalready
widelycollected?
Yes.Can
|     | potentiallybe |     | Unclear |
| --- | ------------- | --- | ------- |
Workloadclassification,
|     | made | Possibletocollect | (highly |
| --- | ---- | ----------------- | ------- |
computeaccounting,detailed
| Training | privacy-preserving | withcustomer | dependent |
| -------- | ------------------ | ------------ | --------- |
workloadverification.
| dataset | usingconfidential | consent. | onimple-    |
| ------- | ----------------- | -------- | ----------- |
|         | computing         |          | mentation). |
techniques.
45

References
Aarne,O.,Fist,T.,andWithers,C. Secure,GovernableChips. Technicalreport,CenterforaNewAmerican
Security,January2024. URLhttps://www.cnas.org/publications/reports/secure-governable-
chips.
Abbott,K.W.,Levi-Faur,D.,andSnidal,D.(eds.). Regulatoryintermediariesintheageofgovernance,volume
670ofTheAnnalsoftheAmericanAcademyofPoliticalandSocialScience. SAGE,March2017a. ISBN
978-1-5063-9011-6. URLhttps://www.jstor.org/stable/i26361533.
Abbott, K.W., Levi-faur, D., andSnidal, D. TheorizingRegulatoryIntermediaries: TheRITModel. The
ANNALSoftheAmericanAcademyofPoliticalandSocialScience, 670(1):14–35, March2017b. ISSN
0002-7162,1552-3349. doi:10.1177/0002716216688272. URLhttp://journals.sagepub.com/doi/
10.1177/0002716216688272.
Advani, A., Elming, W., and Shaw, J. The Dynamic Effects of Tax Audits. The Review of Economics
andStatistics,105(3):545–561,May2023. ISSN0034-6535. doi: 10.1162/rest_a_01101. URLhttps:
//doi.org/10.1162/rest_a_01101.
Ahmed,N.andWahed,M. TheDe-democratizationofAI:DeepLearningandtheComputeDivideinArtificial
IntelligenceResearch,October2020. URLhttp://arxiv.org/abs/2010.15581. arXiv:2010.15581[cs].
Alderman,L.Ireland’sDaysasaTaxHavenMayBeEnding,butNotWithoutaFight.TheNewYorkTimes,July
2021.ISSN0362-4331.URLhttps://www.nytimes.com/2021/07/08/business/ireland-minimum-
corporate-tax.html.
Alibaba. AlibabaClusterTraceProgram,March2024. URLhttps://github.com/alibaba/clusterdata.
original-date:2017-09-05T03:16:34Z.
Allen,G.C. ChokingoffChina’sAccesstotheFutureofAI. Technicalreport,CenterforStrategicandInter-
nationalStudies,October2022. URLhttps://www.csis.org/analysis/choking-chinas-access-
future-ai.
Allen, G. C., Benson, E., and Putnam, M. Japan and the Netherlands Announce Plans for New Export
Controls on Semiconductor Equipment. Commentary, Center for Strategic and International Studies,
April 2023. URL https://www.csis.org/analysis/japan-and-netherlands-announce-plans-
new-export-controls-semiconductor-equipment.
Amazon.com, Inc. An update on Amazon’s efforts to combat child sexual abuse material,
April 2023a. URL https://www.aboutamazon.com/news/policy-news-views/amazon-csam-
transparency-report-2022. Section:Policynews&views.
Amazon.com,Inc.AmazonandAnthropicAnnounceStrategicCollaborationtoAdvanceGenerativeAI,Septem-
ber 2023b. URL https://press.aboutamazon.com/2023/9/amazon-and-anthropic-announce-
strategic-collaboration-to-advance-generative-ai.
Amazon.com, Inc. Sustainability Amazon, 2024. URL https://sustainability.aboutamazon.com/
products-services/the-cloud.
AMD. AMDRegulatoryTradeCompliance,2024. URLhttps://www.amd.com/en/legal/compliance/
trade-compliance.html.
Anderljung,M.,Barnhart,J.,Korinek,A.,Leung,J.,O’Keefe,C.,Whittlestone,J.,Avin,S.,Brundage,M.,
Bullock,J.,Cass-Beggs,D.,Chang,B.,Collins,T.,Fist,T.,Hadfield,G.,Hayes,A.,Ho,L.,Hooker,S.,
Horvitz,E.,Kolt,N.,Schuett,J.,Shavit,Y.,Siddarth,D.,Trager,R.,andWolf,K. FrontierAIRegulation:
ManagingEmergingRiskstoPublicSafety,November2023a.URLhttp://arxiv.org/abs/2307.03718.
arXiv:2307.03718[cs].
Anderljung, M., Smith, E. T., O’Brien, J., Soder, L., Bucknall, B., Bluemke, E., Schuett, J., Trager, R.,
Strahm, L., and Chowdhury, R. Towards Publicly Accountable Frontier LLMs: Building an Exter-
nal Scrutiny Ecosystem under the ASPIRE Framework. Technical report, Centre for the Governance
ofAI,November2023b. URLhttps://www.governance.ai/research-paper/towards-publicly-
accountable-frontier-llms. arXiv:2311.14711[cs].
Anthropic. AnthropicPartnerswithGoogleCloud,February2023. URLhttps://www.anthropic.com/
news/anthropic-partners-with-google-cloud.
46

AustralianAttorney-General’sDepartment. DataRetention:GuidelineforServiceProviders. Technicalreport,
AustralianGovernment,July2015. URLhttps://www.homeaffairs.gov.au/nat-security/files/
data-retention-guidelines-service-providers.pdf.
Australian DITRDCA. International Air Services Information Memorandum, January 2024. URL
https://www.infrastructure.gov.au/infrastructure-transport-vehicles/aviation/
international-aviation/air-services-agreements-arrangements/international-air-
services-information-memorandum. LastModified:2024-01-18Publisher:DepartmentofInfrastruc-
ture,Transport,RegionalDevelopment,CommunicationsandtheArts.
Aviation Transport Security Act. Aviation Transport Security Regulations, 2005. URL https://www8.
austlii.edu.au/cgi-bin/viewdb/au/legis/cth/consol_reg/atsr2005457/.
AWS. General Data Protection Regulation (GDPR) Center, 2024a. URL https://aws.amazon.com/
compliance/gdpr-center/.
AWS. AWSCustomerAgreement,2024b. URLhttps://aws.amazon.com/agreement/#:~:text=You%
20consent%20to%20the%20storage,order%20of%20a%20governmental%20body.
AWS. AWS Global Infrastructure, 2024c. URL https://aws.amazon.com/about-aws/global-
infrastructure/.
AWS. AWSNitroEnclaves,2024d. URLhttps://aws.amazon.com/ec2/nitro/nitro-enclaves/.
AWS. Amazon EC2 On-Demand Pricing, 2024e. URL https://aws.amazon.com/ec2/pricing/on-
demand/.
AWS. AmazonEC2ReservedInstances,2024f. URLhttps://aws.amazon.com/ec2/pricing/reserved-
instances/.
AWS. AWSPrivacyNotice,2024g. URLhttps://aws.amazon.com/privacy/.
AWS. SecurityoftheAWSInfrastructure,2024h. URLhttps://docs.aws.amazon.com/whitepapers/
latest/introduction-aws-security/security-of-the-aws-infrastructure.html.
Banjongkan,A.,Pongsena,W.,Chanklan,R.,Kerdprasop,N.,andKerdprasop,K. Multi-labelclassification
ofhighperformancecomputingworkloadwithvariabletransformation. InternationalJournalofMachine
LearningandComputing,8:536–541,December2018. doi: 10.18178/ijmlc.2018.8.6.742. URLhttps:
//www.ijmlc.org/vol8/742-ML0023.pdf.
BBC. EU-USPrivacyShieldfordatastruckdownbycourt. BBCNews,July2020. URLhttps://www.bbc.
com/news/technology-53418898.
Belfield,H.andHua,S.-S. ComputeandAntitrust:RegulatoryimplicationsoftheAIhardwaresupplychain,
fromchipdesigntocloudAPIs. Verfassungsblog,August2022. URLhttps://verfassungsblog.de/
compute-and-antitrust/.
Besiroglu, T., Bergerson, S.A., Michael, A., Heim, L., Luo, X., andThompson, N. TheComputeDivide
in Machine Learning: A Threat to Academic Contribution and Scrutiny?, January 2024. URL http:
//arxiv.org/abs/2401.02452. arXiv:2401.02452[cs].
Biden,J.R. S.1738-110thCongress(2007-2008):PROTECTOurChildrenActof2008,October2008. URL
https://www.congress.gov/bill/110th-congress/senate-bill/1738. ArchiveLocation: 2007-
06-28.
Boyle, A. and Lau, T. The President’s Extraordinary Sanctions Powers, July 2021. URL
https://www.brennancenter.org/our-work/research-reports/presidents-extraordinary-
sanctions-powers.
Buttarelli,G. TheEU-U.S.PrivacyShieldtwoyearson,March2018. URLhttps://www.edps.europa.eu/
press-publications/press-news/blog/eu-us-privacy-shield-two-years.
California Energy Commission. Power Plant Licensing, 2024. URL https://www.energy.ca.gov/
programs-and-topics/topics/power-plants/power-plant-licensing. Publisher:CaliforniaEn-
ergyCommission.
CenterforOpenScience. BrainsCANComputationalCoreNeuroimagingWiki,March2019. URLhttps:
//osf.io/k89fh/. Publisher:OSF.
47

China Law Translate. 中华人民共和国国家情报法(2018修正), June 2017. URL https://www.
chinalawtranslate.com/national-intelligence-law-of-the-p-r-c-2017/.
Choi,D.,Shavit,Y.,andDuvenaud,D. ToolsforVerifyingNeuralModels’TrainingData,July2023. URL
http://arxiv.org/abs/2307.00682. arXiv:2307.00682[cs].
CodeofFederalRegulations. 22CFRPart120-PurposeandDefinitions,2024. URLhttps://www.ecfr.
gov/current/title-22/part-120.
Confidential Computing Consortium. Confidential Computing: Hardware-Based Trusted Execution
for Applications and Data. Technical report, Confidential Computing Consortium, November
2022.URLhttps://confidentialcomputing.io/wp-content/uploads/sites/10/2023/03/CCC_
outreach_whitepaper_updated_November_2022.pdf.
Congressional Research Service. Who Regulates Whom? An Overview of the U.S. Financial Regulatory
Framework. CRSReportR44918,CongressionalResearchService,October2023. URLhttps://sgp.fas.
org/crs/misc/R44918.pdf.
CongressionalResearchService. TheInternationalEmergencyEconomicPowersAct:Origins,Evolution,and
Use. CRSReportR45618,CongressionalResearchService,January2024. URLhttps://sgp.fas.org/
crs/natsec/R45618.pdf.
Consumer Financial Protection Bureau. CFPB Proposes New Federal Oversight of Big Tech Com-
panies and Other Providers of Digital Wallets and Payment Apps, November 2023. URL https:
//www.consumerfinance.gov/about-us/newsroom/cfpb-proposes-new-federal-oversight-
of-big-tech-companies-and-other-providers-of-digital-wallets-and-payment-apps/.
Copos,B.andPeisert,S. CatchMeIfYouCan:UsingPowerAnalysistoIdentifyHPCActivity,May2020.
URLhttp://arxiv.org/abs/2005.03135. arXiv:2005.03135[cs].
CoreWeave. PrivacyPolicy,October2022. URLhttps://docs.coreweave.com/policies/terms-of-
service/privacy-policy.
CoreWeave. Security&Compliance,2023. URLhttps://docs.coreweave.com/policies/terms-of-
service/security-and-compliance.
Cottier,B. TrendsintheDollarTrainingCostofMachineLearningSystems,January2023. URLhttps://
epochai.org/blog/trends-in-the-dollar-training-cost-of-machine-learning-systems.
CounciloftheEuropeanUnion. ProposalforaRegulationoftheEuropeanParliamentandoftheCouncillaying
downharmonisedrulesonartificialintelligence(ArtificialIntelligenceAct)andamendingcertainUnion
legislativeacts,January2024. URLhttps://data.consilium.europa.eu/doc/document/ST-5662-
2024-INIT/en/pdf.
CountryLegalFrameworksResource. ProvisionofReal-timeLawfulInterceptionAssistance,2023. URL
https://clfr.globalnetworkinitiative.org/country/france/.
Cox, J. Inside the Underground Site Where ‘Neural Networks’ Churn Out Fake IDs, February 2024.
URL https://www.404media.co/inside-the-underground-site-where-ai-neural-networks-
churns-out-fake-ids-onlyfake/.
Dettmers, T., Lewis, M., Belkada, Y., and Zettlemoyer, L. LLM.int8(): 8-bit Matrix Multiplication for
TransformersatScale,November2022. URLhttp://arxiv.org/abs/2208.07339. arXiv:2208.07339
[cs].
ECFR. Acceptanceandscreeningofindividualsandaccessibleproperty.,2024. URLhttps://www.ecfr.
gov/current/title-49/part-1544/section-1544.201.
Egan, J. and Heim, L. Oversight for Frontier AI through a Know-Your-Customer Scheme for
Compute Providers. Technical report, Centre for the Governance of AI, October 2023. URL
https://www.governance.ai/research-paper/oversight-for-frontier-ai-through-kyc-
scheme-for-compute-providers.
EU Agency for Cybersecurity. Safe Harbor Privacy Principles, July 2000. URL https:
//www.enisa.europa.eu/topics/risk-management/current-risk/laws-regulation/data-
protection-privacy/safe-harbor-privacy-principles.
European Commission. EU-U.S. Privacy Shield: Frequently Asked Questions, July 2016. URL https:
//ec.europa.eu/commission/presscorner/detail/hr/MEMO_16_2462.
48

European Commission. Commission welcomes G7 leaders’ agreement on Guiding Principles and a Code
of Conduct on Artificial Intelligence, October 2023a. URL https://ec.europa.eu/commission/
presscorner/detail/en/ip_23_5379.
European Commission. Shaping Europe’s digital future: Hiroshima Process International Code of Con-
ductforAdvancedAISystems,October2023b. URLhttps://digital-strategy.ec.europa.eu/en/
library/hiroshima-process-international-code-conduct-advanced-ai-systems.
EuropeanUnion. Directive2011/93/EUoftheEuropeanParliamentandoftheCouncilof13December2011on
combatingthesexualabuseandsexualexploitationofchildrenandchildpornography,andreplacingCouncil
FrameworkDecision2004/68/JHA,July2011. URLhttps://eur-lex.europa.eu/eli/dir/2011/93/
oj.
EuropeanUnion. Regulation(EU)2016/679oftheEuropeanParliamentandoftheCouncilof27April2016on
theprotectionofnaturalpersonswithregardtotheprocessingofpersonaldataandonthefreemovement
ofsuchdata, andrepealingDirective95/46/EC(GeneralDataProtectionRegulation), May2016. URL
http://data.europa.eu/eli/reg/2016/679/oj. 119.
EuropeanUnion. Regulation(EU)2021/784oftheEuropeanParliamentandoftheCouncilof29April2021on
addressingthedisseminationofterroristcontentonline. OfficialJournaloftheEuropeanUnionL172/79,pp.
79–109,May2021. URLhttps://eur-lex.europa.eu/eli/reg/2021/784/oj.
Farrell,H.andNewman,A. UndergroundEmpire: HowAmericaWeaponizedtheWorldEconomy. Henry
HoltandCo.,September2023. ISBN978-1-250-84055-4. URLhttps://us.macmillan.com/books/
9781250840554/undergroundempire.
FederalRegister. TakingAdditionalStepsToAddresstheNationalEmergencyWithRespecttoSignificant
MaliciousCyber-EnabledActivities:AProposedRulebytheCommerceDepartment,January2024. URL
https://www.federalregister.gov/documents/2024/01/29/2024-01580/taking-additional-
steps-to-address-the-national-emergency-with-respect-to-significant-malicious.
FederalTradeCommission. FTCLaunchesInquiryintoGenerativeAIInvestmentsandPartnerships,January
2024. URLhttps://www.ftc.gov/news-events/news/press-releases/2024/01/ftc-launches-
inquiry-generative-ai-investments-partnerships.
FedRAMP. UnderstandingBaselinesandImpactLevelsforFedRAMPAuthorization,2024. URLhttps:
//www.fedramp.gov/baselines/.
Financial Action Task Force. FATF 40 Recommendations October 2003 (incorporating all subse-
quent amendments until October 2004). Technical report, FATF, October 2003. URL https:
//www.fatf-gafi.org/content/dam/fatf-gafi/recommendations/FATF%20Standards%20-
%2040%20Recommendations%20rc.pdf.
Financial Action Task Force. International Standards on Combating Money Laundering and the
Financing of Terrorism and Proliferation. Technical report, FATF, Paris, France, November
2023. URL https://www.fatf-gafi.org/content/dam/fatf-gafi/recommendations/FATF%
20Recommendations%202012.pdf.coredownload.inline.pdf.
FinancialActionTaskForce. High-riskandothermonitoredjurisdictions,2024a. URLhttps://www.fatf-
gafi.org/en/topics/high-risk-and-other-monitored-jurisdictions.html.
FinancialActionTaskForce. FinancialActionTaskForceHome,2024b. URLhttps://www.fatf-gafi.
org/en/home.html.
Financial Crimes Enforcement Network. FACT SHEET for Section 312 of the USA PATRIOT Act
Final Regulation and Notice of Proposed Rulemaking. Technical report, U.S. Treasury, Decem-
ber 2005. URL https://www.fincen.gov/fact-sheet-section-312-usa-patriot-act-final-
regulation-and-notice-proposed-rulemaking.
Financial Crimes Enforcement Network. Financial Crimes Enforcement Network - Mission, 2024. URL
https://www.fincen.gov/about/mission.
Fist,T.andGrunewald,E. PreventingAIChipSmugglingtoChina. WorkingPaper,CenterforaNewAmeri-
canSecurity,October2023. URLhttps://www.cnas.org/publications/reports/preventing-ai-
chip-smuggling-to-china.
Fist, T., Heim, L., and Schneider, J. Chinese Firms Are Evading Chip Controls, June 2023.
URL https://foreignpolicy.com/2023/06/21/china-united-states-semiconductor-chips-
sanctions-evasion/.
49

FluidStack. FluidStack Privacy Notice, February 2022. URL https://uploads-ssl.webflow.com/
64e49a6c77bc12449a05e6a2/6502008478387e54d7816888_Privacy%20Policy.pdf.
Future of Life Institute. EU Artificial Intelligence Act: The Act Texts, 2024. URL https://
artificialintelligenceact.eu/the-act/.
Gatlan, S. Microsoft breach led to theft of 60,000 US State Dept emails, September 2023.
URL https://www.bleepingcomputer.com/news/security/microsoft-breach-led-to-theft-
of-60-000-us-state-dept-emails/.
Google. google/cluster-data,March2024. URLhttps://github.com/google/cluster-data. original-
date:2015-07-29T17:52:23Z.
GoogleCloud. GoogleCloud&theGeneralDataProtectionRegulation(GDPR),2021. URLhttps://cloud.
google.com/privacy/gdpr.
GoogleCloud. CloudDataProcessingAddendum,November2023. URLhttps://cloud.google.com/
terms/data-processing-addendum.
GoogleCloud. Allnetworkingpricing,2024a. URLhttps://cloud.google.com/vpc/network-pricing.
GoogleCloud. ClimateSustainability,2024b. URLhttps://cloud.google.com/gov/sustainability.
GoogleCloud. GoogleCloudPrivacyNotice,2024c. URLhttps://cloud.google.com/terms/cloud-
privacy-notice.
GovernmentofIndia. Govtconsideringproposaltosetup25KGPUs,October2023. URLhttps://indbiz.
gov.in/govt-considering-proposal-to-set-up-25k-gpus/.
Hacker,P. TheEuropeanAIliabilitydirectives–Critiqueofahalf-heartedapproachandlessonsforthefuture.
ComputerLaw&SecurityReview,51:105871,November2023. ISSN0267-3649. doi:10.1016/j.clsr.2023.
105871. URLhttps://www.sciencedirect.com/science/article/pii/S026736492300081X.
Hay,J.R.andShleifer,A. Privateenforcementofpubliclaws:atheoryoflegalreform. AmericanEconomic
ReviewPapersandProceedings,88(2):398–403,1998. URLhttps://www.jstor.org/stable/116955.
Heim,L. CrucialConsiderationsforComputeGovernance,February2024. URLhttps://blog.heim.xyz/
crucial-considerations-for-compute-governance/.
Heim,L.andEgan,J. AccessingControlledAIChipsviaInfrastructure-as-a-Service(IaaS):Implicationsfor
ExportControls:CommentonBIS–2022–0025(RIN0694–AI94)—Question1. Technicalreport,Centrefor
theGovernanceofAI,December2023. URLhttps://cdn.governance.ai/Accessing_Controlled_
AI_Chips_via_Infrastructure-as-a-Service.pdf.
IBM. What is Confidential Computing?, 2024. URL https://www.ibm.com/topics/confidential-
computing.
India’s Ministry of Electronics and Information Technology. Proposed Digital India Act, 2023, March
2023. URL https://www.meity.gov.in/writereaddata/files/DIA_Presentation%2009.03.
2023%20Final.pdf.
Janardhan,S. ReimaginingOurInfrastructurefortheAIAge,May2023. URLhttps://about.fb.com/
news/2023/05/metas-infrastructure-for-ai/.
Jeon,M.,Venkataraman,S.,Phanishayee,A.,Qian,J.,Xiao,W.,andYang,F. AnalysisofLarge-ScaleMulti-
TenantGPUClustersforDNNTrainingWorkloads,August2019. URLhttp://arxiv.org/abs/1901.
05758. arXiv:1901.05758[cs].
Jiang,B.andCao,A. Chinatocreateandimplementnationalstandardforlargelanguagemodelsinmove
to regulate AI, while using its power to transform industries. South China Morning Post, July 2023.
URL https://www.scmp.com/tech/policy/article/3226942/china-create-and-implement-
national-standard-large-language-models-move-regulate-ai-while-using-its.
Jones, G., Egan, J., and Rosenbach, E. Advancing in Adversity: Ukraine’s Battlefield Technolo-
gies and Lessons for the U.S. Policy Brief, Belfer Center for Science and International Affairs,
July2023.URLhttps://www.belfercenter.org/publication/advancing-adversity-ukraines-
battlefield-technologies-and-lessons-us.
Kim,C. PrivacyactivistsslamEU-USpactondatasharing. BBCNews,July2023. URLhttps://www.bbc.
com/news/world-us-canada-66161135.
50

Korolov, M. Data centers unprepared for new European energy efficiency regulations, December 2023.
URL https://www.networkworld.com/article/1251883/data-centers-unprepared-for-new-
european-energy-efficiency-regulations.html.
Kulp,G.,Gonzales,D.,Smith,E.,Heim,L.,Puri,P.,Vermeer,M.J.D.,andWinkelman,Z. Hardware-Enabled
GovernanceMechanisms: DevelopingTechnicalSolutionstoExemptItemsOtherwiseClassifiedUnder
ExportControlClassificationNumbers3A090and4A090. Technicalreport,RANDCorporation,January
2024. URLhttps://www.rand.org/pubs/working_papers/WRA3056-1.html.
Köhler,S.,Wenzel,L.,Plauth,M.,Böning,P.,Gampe,P.,Geier,L.,andPolze,A. RecognizingHPCWorkloads
BasedonPowerDrawSignatures. In2021NinthInternationalSymposiumonComputingandNetworking
Workshops(CANDARW),pp.278–284,December2021. doi:10.1109/CANDARW53999.2021.00053. URL
https://ieeexplore.ieee.org/document/9644213.
LambdaLabs. LambdaPrivacyPolicy,August2022. URLhttps://lambdalabs.com/legal/privacy-
policy.
legislation.gov.uk. Data Retention and Investigatory Powers Act 2014, 2014. URL https:
//www.legislation.gov.uk/ukpga/2014/27/crossheading/retention-of-relevant-
communications-data/enacted. Publisher:King’sPrinterofActsofParliament.
Linn,C.J. RedefiningtheBankSecrecyAct:CurrencyReportingandtheCrimeofStructuring. SantaClara
LawReview,50(2):407–513,January2010. URLhttps://digitalcommons.law.scu.edu/lawreview/
vol50/iss2/4/.
Lohr, A. Intelligence community and Defense Department to share classified cloud services,
July 2023. URL https://federalnewsnetwork.com/defense-main/2023/07/intelligence-
community-and-defense-department-to-share-classified-cloud-services/.
Merritt,R. WhatIsNVLink?,March2023. URLhttps://blogs.nvidia.com/blog/what-is-nvidia-
nvlink/.
Microsoft. USNationalSecurityOrdersReports|MicrosoftCSR,2022. URLhttps://www.microsoft.
com/en-us/corporate-responsibility/fisa.
Microsoft. What is confidential computing?, October 2023. URL https://learn.microsoft.com/en-
us/azure/confidential-computing/overview.
Microsoft. Microsoft Privacy Statement – Microsoft privacy, February 2024a. URL https://privacy.
microsoft.com/en-us/privacystatement.
Microsoft. ConfidentialComputingonAzure,February2024b. URLhttps://learn.microsoft.com/en-
us/azure/confidential-computing/overview-azure-products.
MicrosoftAzure. AzureSustainability,2024a. URLhttps://azure.microsoft.com/en-us/explore/
global-infrastructure/sustainability.
Microsoft Azure. Bandwidth pricing, 2024b. URL https://azure.microsoft.com/en-us/pricing/
details/bandwidth/.
MicrosoftCorporateBlogs. MicrosoftandOpenAIextendpartnership,January2023. URLhttps://blogs.
microsoft.com/blog/2023/01/23/microsoftandopenaiextendpartnership/.
Milmo, D. CMA to investigate UK cloud computing market amid Microsoft and Amazon concerns. The
Guardian, October2023. ISSN0261-3077. URLhttps://www.theguardian.com/business/2023/
oct/05/amazon-and-microsofts-uk-cloud-computing-dominance-faces-investigation.
MithrilSecurity. mithril-security/aicert,January2024a. URLhttps://github.com/mithril-security/
aicert. original-date:2023-07-04T07:24:29Z.
MithrilSecurity.mithril-security/blindai,February2024b.URLhttps://github.com/mithril-security/
blindai. original-date:2022-02-06T14:07:35Z.
Mulani,N.andWhittlestone,J. ProposingaFoundationModelInformation-SharingRegimefortheUK,June
2023. URLhttps://www.governance.ai/post/proposing-a-foundation-model-information-
sharing-regime-for-the-uk.
Murgia,M. WhiteHousesciencechiefsignalsUS-Chinaco-operationonAIsafety. FinancialTimes,January
2024. URLhttps://www.ft.com/content/94b9878b-9412-4dbc-83ba-aac2baadafd9.
51

Nagao, R. Japan to pay for half of $100m generative AI supercomputer - Nikkei Asia. Nikkei Asia,
June2023. URLhttps://asia.nikkei.com/Business/Technology/Japan-to-pay-for-half-of-
100m-generative-AI-supercomputer.
NationalEnergyResearchScientificComputing. NERSCDocumentation:RooflinePerformanceModel,2024.
URLhttps://docs.nersc.gov/tools/performance/roofline/.
NationalSecurityTelecommunicationsAdvisoryCommittee. NSTACReporttothePresident: Addressing
theAbuseofDomesticInfrastructurebyForeignMaliciousActors. Technicalreport, NationalSecurity
Telecommunications Advisory Committee, 2023. URL https://www.cisa.gov/sites/default/
files/2024-01/NSTAC_Report_to_the_President_on_Addressing_the_Abuse_of_Domestic_
Infrastructure_by_Foreign_Malicious_Actors_508c.pdf.
Nevo,S.,Lahav,D.,Karpur,A.,Alstott,J.,andMatheny,J. SecuringArtificialIntelligenceModelWeights:
InterimReport.Technicalreport,RANDCorporation,October2023.URLhttps://www.rand.org/pubs/
working_papers/WRA2849-1.html.
NVIDIA. ConfidentialComputeonNVIDIAHopperH100,July2023. URLhttps://images.nvidia.com/
aem-dam/en-zz/Solutions/data-center/HCC-Whitepaper-v1.0.pdf.
NVIDIA. NVIDIABlueFieldNetworkingPlatform,2024a. URLhttps://resources.nvidia.com/en-us-
accelerated-networking-resource-library-ms/.
NVIDIA. NVIDIANsightPerfSDK,2024b. URLhttps://developer.nvidia.com/nsight-perf-sdk.
NVIDIA. RedfishAPIsSupport,2024c. URLhttps://docs.nvidia.com/dgx/dgxh100-user-guide/
redfish-api-supp.html.
O’Brien,J.,Ee,S.,andWilliams,Z. Deploymentcorrections:AnincidentresponseframeworkforfrontierAI
models. Technicalreport,InstituteforAIPolicyandStrategy,September2023. URLhttps://arxiv.org/
abs/2310.00328.
OECD. Measuring the environmental impacts of artificial intelligence compute and applica-
tions: The AI footprint. OECD Digital Economy Papers 341, OECD, November 2022. URL
https://www.oecd-ilibrary.org/science-and-technology/measuring-the-environmental-
impacts-of-artificial-intelligence-compute-and-applications_7babf571-en. Series:
OECDDigitalEconomyPapersVolume:341.
Office for Civil Rights. Guidance on HIPAA & Cloud Computing, October 2016. URL
https://www.hhs.gov/hipaa/for-professionals/special-topics/health-information-
technology/cloud-computing/index.html. LastModified:2023-02-02T10:24:50-0500.
OFWAT. TheWaterServicesRegulationAuthority,2024. URLhttps://www.ofwat.gov.uk/regulated-
companies/ofwat-industry-overview/licences/.
OpenMined. HowtoAuditanAIModelOwnedbySomeoneElse(Part1):Anintroductiontostate-of-the-art
AIauditinginfrastructure,June2023. URLhttps://blog.openmined.org/ai-audit-part-1/.
OpenMined. OpenMined/PySyft,March2024. URLhttps://github.com/OpenMined/PySyft. original-
date:2017-07-18T20:41:16Z.
Owen,D. Howpredictableislanguagemodelbenchmarkperformance?,January2024. URLhttp://arxiv.
org/abs/2401.04757. arXiv:2401.04757[cs].
Pal,B.,Gorczynski,S.,andSchmidt,D. OverviewofDataTransferCostsforCommonArchitectures|AWS
ArchitectureBlog,June2021. URLhttps://aws.amazon.com/blogs/architecture/overview-of-
data-transfer-costs-for-common-architectures/. Section:AmazonEC2.
Patel,P.,Choukse,E.,Zhang,C.,Goiri,I.,Warrier,B.,Mahalingam,N.,andBianchini,R. POLCA:Power
OversubscriptioninLLMCloudProviders, August2023. URLhttp://arxiv.org/abs/2308.12908.
arXiv:2308.12908[cs].
Pilz,K.andHeim,L. ComputeatScale:ABroadInvestigationintotheDataCenterIndustry,November2023.
URLhttps://arxiv.org/abs/2311.02651v4.
Pilz,K.,Heim,L.,andBrown,N. IncreasedComputeEfficiencyandtheDiffusionofAICapabilities,February
2024. URLhttp://arxiv.org/abs/2311.15377. arXiv:2311.15377[cs].
52

PrimeMinister’sOffice,FCDOUK,andDSITUK. TheBletchleyDeclarationbyCountriesAttendingtheAI
Safety Summit, 1-2 November 2023, November 2023. URL https://www.gov.uk/government/
publications/ai-safety-summit-2023-the-bletchley-declaration/the-bletchley-
declaration-by-countries-attending-the-ai-safety-summit-1-2-november-2023.
Rabinovitsj,D. OpeningAIInfrastructure:UsheringInTheAgeOfGenAI,December2023. URLhttps://
drive.google.com/file/d/1ud1JZqco2868AvmkNkrA-Axp-74PvwWx/view?usp=embed_facebook.
Rep. Collins, D. R.-G.-. Text - H.R.4943 - 115th Congress (2017-2018): CLOUD Act, February 2018.
URLhttps://www.congress.gov/bill/115th-congress/house-bill/4943/text. ArchiveLoca-
tion:2018-02-06.
Richter, F. Amazon Maintains Cloud Lead as Microsoft Edges Closer, February 2024. URL
https://www.statista.com/chart/18819/worldwide-market-share-of-leading-cloud-
infrastructure-service-providers.
Sanction Scanner. What is the Difference Between Smurfing and Structuring?, 2024. URL
https://sanctionscanner.com/blog/what-is-the-difference-between-smurfing-and-
structuring-594.
Sastry,G.,Heim,L.,Belfield,H.,Anderljung,M.,Brundage,M.,Hazell,J.,O’Keefe,C.,Hadfield,G.K.,
Ngo,R.,Pilz,K.,Gor,G.,Bluemke,E.,Shoker,S.,Egan,J.,Trager,R.F.,Avin,S.,Weller,A.,Bengio,
Y.,andCoyle,D. ComputingPowerandtheGovernanceofArtificialIntelligence,February2024. URL
http://arxiv.org/abs/2402.08797. arXiv:2402.08797[cs].
Secretary of State for Science, Innovation and Technology. A pro-innovation approach to AI regulation.
Policy paper Command Paper Number: 815, GOV.UK., August 2023. URL https://www.gov.uk/
government/publications/ai-regulation-a-pro-innovation-approach/white-paper. ISBN:
978-1-5286-4009-1.
Senator Scott Wiener. Senator Wiener Introduces Legislation to Ensure Safe Development of
Large-Scale Artificial Intelligence Systems and Support AI Innovation in California, Febru-
ary 2024. URL https://sd11.senate.ca.gov/news/20240208-senator-wiener-introduces-
legislation-ensure-safe-development-large-scale-artificial.
Sevilla,J.,Heim,L.,Ho,A.,Besiroglu,T.,Hobbhahn,M.,andVillalobos,P. ComputeTrendsAcrossThree
ErasofMachineLearning. In2022InternationalJointConferenceonNeuralNetworks(IJCNN),pp.1–
8, July 2022. doi: 10.1109/IJCNN55064.2022.9891914. URL http://arxiv.org/abs/2202.05924.
arXiv:2202.05924[cs].
Shavit,Y.,Agarwal,S.,Brundage,M.,andAdler,S. PracticesforGoverningAgenticAISystems. ResearchPa-
per,OpenAI,December2023. URLhttps://cdn.openai.com/papers/practices-for-governing-
agentic-ai-systems.pdf.
Sheehan, M. Tracing the Roots of China’s AI Regulations. Technical report, Carnegie Endowment for
InternationalPeace,February2024. URLhttps://carnegieendowment.org/2024/02/27/tracing-
roots-of-china-s-ai-regulations-pub-91815.
Shoeybi, M., Patwary, M., Puri, R., LeGresley, P., Casper, J., and Catanzaro, B. Megatron-LM: Training
Multi-BillionParameterLanguageModelsUsingModelParallelism,March2020. URLhttp://arxiv.
org/abs/1909.08053. arXiv:1909.08053[cs].
Sliwko,L.andGetov,V. AGOCS—AccurateGoogleCloudSimulatorFramework. In2016IntlIEEEConfer-
encesonUbiquitousIntelligence&Computing,AdvancedandTrustedComputing,ScalableComputingand
Communications,CloudandBigDataComputing,InternetofPeople,andSmartWorldCongress(UIC/ATC/S-
calCom/CBDCom/IoP/SmartWorld), pp. 550–558, January 2016. doi: 10.1109/UIC-ATC-ScalCom-
CBDCom-IoP-SmartWorld.2016.0095. URLhttps://ieeexplore.ieee.org/document/7816891.
Smith,B.TheneedforaDigitalGenevaConvention,February2017.URLhttps://blogs.microsoft.com/
on-the-issues/2017/02/14/need-digital-geneva-convention/.
Smith,B.HowdowebestgovernAI?,May2023.URLhttps://blogs.microsoft.com/on-the-issues/
2023/05/25/how-do-we-best-govern-ai/.
Tang, B. J., Chen, Q., Weiss, M. L., Frey, N., McDonald, J., Bestor, D., Yee, C., Arcand, W., Byun, C.,
Edelman, D., Hubbell, M., Jones, M., Kepner, J., Klein, A., Michaleas, A., Michaleas, P., Milechin, L.,
Mullen, J., Prout, A., Reuther, A., Rosa, A., Bowne, A., McEvoy, L., Li, B., Tiwari, D., Gadepally, V.,
and Samsi, S. The MIT Supercloud Workload Classification Challenge. In 2022 IEEE International
Parallel and Distributed Processing Symposium Workshops (IPDPSW), pp. 708–714, May 2022. doi:
10.1109/IPDPSW55747.2022.00122. URLhttp://arxiv.org/abs/2204.05839. arXiv:2204.05839[cs].
53

Terai,M.,Kashiwaki,R.,andShoji,F. WorkloadClassificationandPerformanceAnalysisusingJobMetrics
in the K computer. IPSJ SIG Technical Report 13, Information Processing Society of Japan, Decem-
ber2017. URLhttps://ipsj.ixsq.nii.ac.jp/ej/?action=repository_uri&item_id=184893&
file_id=1&file_no=1. Vol.2017-HPC-162.
The European High Performance Computing Joint Undertaking. Open Call to Support HPC-
powered Artificial Intelligence (AI) Applications - European Commission, November 2023.
URL https://eurohpc-ju.europa.eu/open-call-support-hpc-powered-artificial-
intelligence-ai-applications-2023-11-28_en.
TheWhiteHouse. VoluntaryAICommitments,September2023a. URLhttps://www.whitehouse.gov/wp-
content/uploads/2023/09/Voluntary-AI-Commitments-September-2023.pdf.
TheWhiteHouse. ExecutiveOrderontheSafe,Secure,andTrustworthyDevelopmentandUseofArtificial
Intelligence. Technicalreport,TheWhiteHouse,October2023b. URLhttps://www.whitehouse.gov/
briefing-room/presidential-actions/2023/10/30/executive-order-on-the-safe-secure-
and-trustworthy-development-and-use-of-artificial-intelligence/.
The White House. FACT SHEET: Biden-Harris Administration Secures Voluntary Commitments from
Leading Artificial Intelligence Companies to Manage the Risks Posed by AI, July 2023c. URL
https://www.whitehouse.gov/briefing-room/statements-releases/2023/07/21/fact-
sheet-biden-harris-administration-secures-voluntary-commitments-from-leading-
artificial-intelligence-companies-to-manage-the-risks-posed-by-ai/.
TheWhiteHouse. G7HiroshimaLeaders’Communiqué,May2023d. URLhttps://www.whitehouse.gov/
briefing-room/statements-releases/2023/05/20/g7-hiroshima-leaders-communique/.
Tirmazi,M.,Barker,A.,Deng,N.,Haque,M.E.,Qin,Z.G.,Hand,S.,Harchol-Balter,M.,andWilkes,J. Borg:
thenextgeneration. InProceedingsoftheFifteenthEuropeanConferenceonComputerSystems,pp.1–14,
HeraklionGreece,April2020.ACM. ISBN978-1-4503-6882-7. doi: 10.1145/3342195.3387517. URL
https://dl.acm.org/doi/10.1145/3342195.3387517.
Trager,R.,Harack,B.,Reuel,A.,Carnegie,A.,Heim,L.,Ho,L.,Kreps,S.,Lall,R.,Larter,O.,ÓhÉigeartaigh,
S.,Staffell,S.,andVillalobos,J.J. InternationalGovernanceofCivilianAI:AJurisdictionalCertification
Approach. Whitepaper, Oxford Martin AI Governance initiative and Centre for the Governance of AI,
August2023. URLhttps://cdn.governance.ai/International_Governance_of_Civilian_AI_
OMS.pdf.
UKDSIT. CapabilitiesandrisksfromfrontierAI:AdiscussionpaperontheneedforfurtherresearchintoAI
risk. Technicalreport,DSITUK,October2023. URLhttps://assets.publishing.service.gov.uk/
media/65395abae6c968000daa9b25/frontier-ai-capabilities-risks-report.pdf.
UKDSITandDonelan,M.TechnologySecretaryannouncesinvestmentboostmakingBritishAIsupercomputing
30timesmorepowerful,November2023. URLhttps://www.gov.uk/government/news/technology-
secretary-announces-investment-boost-making-british-ai-supercomputing-30-times-
more-powerful.
UK Government. AI Safety Summit 2023 - GOV.UK, February 2024. URL https://www.gov.uk/
government/topical-events/ai-safety-summit-2023.
UK Research and Innovation. £300 million to launch first phase of new AI Research Resource, Novem-
ber2023.URLhttps://www.ukri.org/news/300-million-to-launch-first-phase-of-new-ai-
research-resource/.
US BIS and US DOC. Implementation of Additional Export Controls: Certain Advanced Computing
Items; Supercomputer and Semiconductor End Use; Updates and Corrections, October 2023. URL
https://www.federalregister.gov/documents/2023/10/25/2023-23055/implementation-of-
additional-export-controls-certain-advanced-computing-items-supercomputer-and.
U.S.NationalScienceFoundation. DemocratizingthefutureofAIR&D:NSFtolaunchNationalAIResearch
Resourcepilot|NSF-NationalScienceFoundation,January2024. URLhttps://new.nsf.gov/news/
democratizing-future-ai-rd-nsf-launch-national-ai.
U.S.SecuritiesandExchangeCommission. RetentionofRecordsRelevanttoAuditsandReviews,March
2003. URLhttps://www.sec.gov/rules/2003/01/retention-records-relevant-audits-and-
reviews.
54

Vailshery,L.S. Worldwideinfrastructureasaservice(IaaS)andplatformasaservice(PaaS)hyperscalermarket
sharefrom2020to2023,byvendor,February2024. URLhttps://www.statista.com/statistics/
1202770/hyperscaler-iaas-paas-market-share/.
Vanian, J. HPE hacked by same Russian intelligence group that hit Microsoft, January
2024. URL https://www.cnbc.com/2024/01/24/hpe-hit-by-russian-intelligence-group-
that-hacked-microsoft.html.
Ward,J.andHu,K. USantitrustinquirytargetsOpenAIandAnthropic’sdealswithBigTech. Reuters,January
2024. URLhttps://www.reuters.com/technology/ftc-launches-inquiry-into-generative-
ai-investments-partnerships-2024-01-25/.
Weiss, M.L., McDonald, J., Bestor, D., Yee, C., Edelman, D., Jones, M., Prout, A., Bowne, A., McEvoy,
L., Gadepally, V., and Samsi, S. An Evaluation of Low Overhead Time Series Preprocessing Tech-
niquesforDownstreamMachineLearning,September2022. URLhttp://arxiv.org/abs/2209.05300.
arXiv:2209.05300[cs].
Weng,Q.,Xiao,W.,Yu,Y.,Wang,W.,Wang,C.,He,J.,Li,Y.,Zhang,L.,Lin,W.,andDing,Y. MLaaSin
thewild:WorkloadanalysisandschedulinginLarge-ScaleheterogeneousGPUclusters. In19thUSENIX
symposiumonnetworkedsystemsdesignandimplementation(NSDI22),pp.945–960,Renton,WA,April
2022.USENIXAssociation. ISBN978-1-939133-27-4. URLhttps://www.usenix.org/conference/
nsdi22/presentation/weng.
Whittlestone,J.andClark,J. WhyandHowGovernmentsShouldMonitorAIDevelopment,August2021. URL
http://arxiv.org/abs/2108.12427. arXiv:2108.12427[cs].
Whittlestone,J.,Avin,S.,Heim,L.,Anderljung,M.,andSastry,G. ResponsetotheUK’sFutureofCompute
Review. Technicalreport,CentrefortheGovernanceofAI,March2023. URLhttps://www.governance.
ai/research-paper/response-to-the-uks-future-of-compute-review.
Wikipediacontributors. Hardwareperformancecounter,August2023. URLhttps://en.wikipedia.org/w/
index.php?title=Hardware_performance_counter&oldid=1169157291.
Williams,S.,Waterman,A.,andPatterson,D. Roofline:AnInsightfulVisualPerformanceModelforFloating-
PointProgramsandMulticoreArchitectures,October2008.URLhttps://people.eecs.berkeley.edu/
~kubitron/cs252/handouts/papers/RooflineVyNoYellow.pdf.
55
