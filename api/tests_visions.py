""" Test cases for the visions module. """

import api.visions
import os
import sqlite3
from time import time
from unittest import TestCase
from unittest.mock import patch


create_viwPREmployees = '''/* SQL create table statement for testing database version of viwPREmployees. */
CREATE TABLE viwPREmployees (
    JobTitle,
    DepartmentDescription,
    Name,
    EmployeeSSN,
    Ethnicity,
    ID,
    EmployeeID,
    LastName,
    FirstName,
    MiddleName,
    JobID,
    EmployeeAddress1,
    EmployeeAddress2,
    EmployeeCity,
    EmployeeState,
    EmployeeZipCode,
    EmployeeHomePhone,
    PayrollStatus,
    Gender,
    DepartmentID,
    BirthDate,
    HireDate,
    TermDate,
    EndProbationDate,
    LeaveBankStartDate,
    BenefitsEligDate,
    SeniorityDate,
    ReHireDate,
    EmergencyContactPhone,
    UserEmployeeID,
    YearsExperience,
    Comments,
    NamePrefix,
    GenerationID,
    WorkPhone,
    WorkPhoneExt,
    tblHRMasterEthnicityID,
    Married,
    PreviousName,
    YearsExpPrevious,
    YearsExpDistrict,
    FamiliarName,
    HRNewEmployee,
    NewHire,
    EmployeeEmail,
    SupressPhone,
    tblPRClassificationID,
    EmergencyAddress1,
    EmergencyAddress2,
    EmergencyCity,
    EmergencyState,
    EmergencyZipCode,
    ConcurrencyID,
    tblPRTerminationCodeID,
    ParticipatesLeaveBank,
    tblPRStatusID,
    IsSubstitute,
    tblPRInsClassID,
    tblPRLeaveBankID,
    EthnicityID,
    Classification,
    Status,
    InsuranceClass,
    LeaveBankPlan,
    TerminationCode,
    tblHRApplicantsID,
    HRNewHire,
    CSZ,
    DOBMonth,
    DOBDay,
    DOBMonthName,
    tblPRTemplateID,
    TemplateName,
    PRGender,
    IssuePayCheck,
    StateCode,
    EEOCClass,
    TenureDate,
    LeaveAccrualDate,
    TotalYears,
    IssuePayCheckText,
    tblHRMasterEEOCClassificationID,
    Department,
    SIFEthnicityCode,
    EEOCCode,
    MaskSSN,
    EmployeeInternetAccess,
    CellPhone,
    StateID,
    UserData1,
    UserData2,
    UserData3,
    UserData4,
    UserData5,
    UserData6,
    UserData7,
    UserData8,
    UserData9,
    UserData10,
    UserData11,
    UserData12,
    UserData13,
    UserData14,
    UserData15,
    UserData16,
    UserData17,
    UserData18,
    UserData19,
    UserData20,
    Class,
    tblGLMedicaidClassID,
    PortalUserName,
    PRMarried,
    tblPREmployeesID,
    InsFrequency,
    InsBenefitAllowance,
    InsBenefitAllowanceNY,
    InsClassDescription,
    CreditedService,
    Frequency,
    TPAFrequency,
    StartPeriod,
    PlanBegin,
    PlanEnd,
    tblPRMasterInsuranceClassID,
    Archive,
    NMTribe,
    NMHQPDTeachers,
    NMHQMSBegTeacher,
    NMHQPDAdmins,
    NMBDI,
    NMHD,
    NMHDI,
    NMTitleIAFTE,
    NMTitleIVFTE,
    NMStatus,
    LocationAddress1,
    LocationAddress2,
    LocationCity,
    LocationState,
    LocationZipCode,
    LocationCode,
    EmpFTE,
    PrimaryWorksite,
    EmailDD,
    tblPRPrimaryWorksitesID,
    COYrsTeachingInState,
    COYrsTeachingOutState,
    COYrsEduInState,
    COYrsEduOutState,
    COYrsPrincipalAny,
    CODistrictResidence,
    COPassParaTest,
    COPassCoreTest,
    COTenure,
    COStateAdminCore,
    ORPERSWageCode,
    ILWorkersCompClass,
    DaysExperience,
    DaysExpPrevious,
    DaysExpDistrict,
    CreditedServiceDays,
    TotalDays,
    LastPaidDate,
    Certified,
    ILLocationStatus,
    ILMonthsEmployed,
    ILPercentTimeAdmin,
    NEUSCitizen,
    CASTRSMembershipError,
    CASTRSBirthDateError,
    NEContractDate,
    NEEducationAttained,
    NEPassParaTest,
    NEContractOrg,
    NELocalContract,
    NEExcludeFromNSSRS,
    ORTSPCID,
    NMtblHRMasterEthnicityID2,
    NMtblHRMasterEthnicityID3,
    NMtblHRMasterEthnicityID4,
    NMtblHRMasterEthnicityID5,
    COTechProficiencyLevel,
    COTechAssessmentType,
    COTechAssessmentDate,
    ILEmploymentType,
    ILLowestGrade,
    ILHighestGrade,
    ILTeachAssignment1,
    ILTeachAssignment2,
    ILTeachAssignment3,
    ILTeachAssignment4,
    ILTeachAssignment5,
    ILTeachAssignment6,
    ILTeachAssignment7,
    ILClassesTaught1,
    ILClassesTaught2,
    ILClassesTaught3,
    ILClassesTaught4,
    ILClassesTaught5,
    ILClassesTaught6,
    ILClassesTaught7,
    ILPercentTimeEmployed,
    HasDocs,
    tblNMTEClassificationID,
    CAARSMemberStatus,
    CAARSRetirementDate,
    CAARSActiveDate,
    CAPERSMemberStatus,
    CAPERSMemberType,
    CAPERSRetirementDate,
    CAPERSActiveDate,
    CAPERSMembershipNumber,
    CASTRSMemberStatus,
    CASTRSMemberType,
    CASTRSRetirementDate,
    CASTRSActiveDate,
    PrimaryWorksiteCode,
    EthnicOrigin,
    tblPRNDPrevEmpTypeID,
    NDYrsAdminExp,
    COTeacherProbationaryStatus,
    COFormalPerformanceEvaluationDate,
    COTeacherPerformance,
    COLAEDID,
    COPrincipalPerformance,
    OKSPRYrsExpOutState,
    OKSPRYrsExpMilitary,
    OKSPRYrsExpInState,
    OKSPRYrsExpDistrict,
    OKTRSYrsExp,
    Smoker,
    BenefitsEligEndDate,
    OKSPRRetired,
    OKSPRResidency,
    OKSPRMentor,
    PREthnicOrigin,
    UniqueName,
    TermStateCode,
    NMYrsExpTeachInDist,
    NMYrsExpTeachOutDist,
    NMYrsExpPrinInDist,
    NMYrsExpPrinOutDist,
    NMYrsExpTeachTotal,
    NMYrsExpPrinTotal,
    BargainingUnit,
    UnionCode,
    tblPRMasterBargainingUnitID,
    tblPRMasterUnionCodeID,
    ILEISExcludeFromEIS,
    ILEISRetired,
    GASHBPEligible,
    ReimbursementRequests,
    GASHBPWeeklyHours,
    ClassificationType,
    WYRAINID,
    Retired,
    IDExcludeFromISEE,
    IDYrsExpInDist,
    IDYrsExpInState,
    IDYrsExpOutState,
    IDYrsExpNonPublic,
    IDYrsExpHigherEdInState,
    IDYrsExpHigherEdOutState,
    IDPara,
    IDTitleIPara,
    PersonalEmail,
    PreferredEmail,
    Email,
    PreferredEmailText,
    COTeachQuality1,
    COTeachQuality2,
    COTeachQuality3,
    COTeachQuality4,
    COTeachQuality5,
    COTeachQuality6,
    COPrinQuality2,
    COPrinQuality1,
    COPrinQuality3,
    COPrinQuality4,
    COPrinQuality5,
    COPrinQuality6,
    COPrinQuality7,
    GAPlanParticipation,
    GAEmployeeType,
    ACAStatus,
    NYEthnicity2,
    NYEthnicity3,
    NYEthnicity4,
    NYEthnicity5,
    NYProfessionalDevelopment,
    NYPrincipalHireDate,
    ExporttoSIS,
    NEPrimarySubjectArea,
    PrivateEmployee,
    TemporaryPrivateEmployee,
    NYStaffSnapshot,
    COEducatorPrepProgram,
    AZEmpType,
    GAPRCJobClassification,
    GAPRCJobStatus,
    GAPRCNoEnrollmentReason,
    AKHiredForSpecialEd,
    AKTitleIHireDate,
    AKTitleIHSDiploma,
    AKSPEDAide,
    AKSPEDAide3_5,
    AKMinQuals,
    AKLimitedCertificate,
    AKNewToState,
    AKNewToProfession,
    AKLongTermSub,
    AKHighlyQualified,
    AKHQMethod,
    AKNotHQReason,
    AKNotHQPlan,
    AKHiredForSPED,
    PrintW2,
    ACAOfferingGroup,
    PAPIMSStaffType,
    PAPIMSEmpStatus,
    MESeasonal,
    GAACA,
    IDIncludeOnISEEForm8,
    IDDateOfLastK12Exp,
    IDPlaceOfLastK12Exp,
    IDProfPerfCriteriaMet,
    RIEdAttend,
    NYItinerantTeacher
);
'''

create_viwPRPositions = '''/* SQL create table statement for testing database version of viwPRPositions. */
CREATE TABLE viwPRPositions (
    ID,
    PositionID,
    tblAPReqLocationsID,
    DAC,
    tblPRDACBudgetedPositionsID,
    PosType,
    Description,
    PositionFTEs,
    BudgetAmt,
    Schedule,
    WorkCalendar,
    tblPRMasterSalaryScheduleCellsID,
    tblPRWorkCalendarsID,
    ConcurrencyID,
    Status,
    EmployeeID,
    Name,
    EmployeeSSN,
    tblPREmployeesID,
    PriorYearAmt,
    Classification,
    PayMethod,
    PayBasis,
    Rate,
    HrsDay,
    IsActive,
    StartDate,
    EndDate,
    PositionDays,
    PositionAmount,
    StateCode,
    SDERPCode,
    ClassCode,
    Category,
    tblPRPositionCategoryID,
    tblPRMasterPositionCodesID,
    tblPRMasterWorkersCompClassCodesID,
    LeaveAccrualFactor,
    SalaryScheduleType,
    NextYearSalaryScheduleCellsID,
    NextYearRow,
    NextYearCol,
    NextYearScheduleAmt,
    Projection,
    NextYearScheduleType,
    SalaryScheduleRow,
    SalaryScheduleCol,
    SalaryScheduleAmt,
    NextYearAmt,
    NextYearRate,
    NextYearFTE,
    NumberFilled,
    PositionRankingID,
    PositionRankingType,
    tblHRMasterContractsID,
    ContractName,
    Type,
    SupervisorID,
    NextEvaluationDate,
    FundingStatus,
    tblHRMasterDepartmentsID,
    Department,
    PayCycle,
    AssignmentStatus,
    TRSCategoryDescription,
    TRSCategory,
    TRSPayUnit,
    TRSYearRoundTFlg,
    TRSNonStdConFlg,
    StartPayPeriod,
    EndPayPeriod,
    tblPRPayPeriodsID_StartPayPeriod,
    tblPRPayPeriodsID_EndPayPeriod,
    SchoolCode,
    EmployeeAddress1,
    EmployeeAddress2,
    EmployeeCity,
    EmployeeState,
    EmployeeZipCode,
    DepartmentDescription,
    DepartmentID,
    ExcludeFromADS,
    UserEmployeeID,
    ReadyToGenerate,
    RecordType,
    LumpSumPeriods,
    IssuePayCheck,
    SDERGradeLevel,
    DailyAmount,
    PayBasisString,
    PayMethodString,
    DistributionType,
    JobTitle,
    ContractAdjustment,
    NVPERSContractDate,
    NVPERSPartTime,
    MTHoursType,
    MTEarningsType,
    IssuePayCheckText,
    NYEmploymentBase,
    NYPayRate,
    NYPositionType,
    NYIndicator,
    tblPRNYBaseHoursID,
    NYBaseHoursCode,
    NYRetro,
    NYRetroYear,
    RowHead,
    ColHead,
    RowHeadNY,
    ColHeadNY,
    PAEmploymentType,
    PAWageType,
    tblPRPAWorkStatusID,
    PAWorkStatusCode,
    PAWorkStatusDescription,
    PAWorkStatusStartDate,
    PAWorkStatusEndDate,
    PAExpectedMonths,
    PAExpectedUnits,
    PAVotingStatus,
    PABocFlag,
    PAOutstandingCredit,
    PABocSvcEndDate,
    ClassificationText,
    ORReportableHours,
    ORPERSPayType,
    tblPRStatusID,
    EmployeeStatus,
    PAReportAnnually,
    ORPERSWageCode,
    NYCivilService,
    TXPopCode,
    TXActivityCode,
    TXServiceCode,
    MaskSSN,
    PositionType,
    IsSubstitute,
    InsuranceClass,
    tblPRPositionTypesID,
    Supervisor,
    AmountFTD,
    NMPERAWageCode,
    NMPERAExcludedReason,
    tblHPPARApprovalTemplateID,
    TemplateName,
    EmployeeClassification,
    ExcludedRetro,
    OneTimePay,
    tblPREmpLeavePlansID,
    LeavePlan,
    WorkCalendarName,
    NYNonABS,
    Expr1,
    AutoStep,
    tblPRMasterSalaryScheduleID,
    NDRateClassification,
    ScheduleDays,
    Comments,
    NextYearScheduleDays,
    ScheduleNY,
    Archive,
    DescType,
    AssignedByHR,
    ExcludeInsurance,
    ExcludeFromUC,
    PAPIMSReportable,
    WorkDays,
    TCIP,
    TCIJob,
    TCIDept,
    SupplementalTemplateID,
    PAPSERSPriorYear,
    AdvanceDate,
    tblPRPositionsID,
    COYrsPrincipalSchool,
    COClassesInSubject,
    COTwentyFourSemesterHours,
    COGradeLevelInfant,
    COGradeLevelPreK,
    COGradeLevelK,
    COGradeLevel1,
    COGradeLevel2,
    COGradeLevel3,
    COGradeLevel4,
    COGradeLevel5,
    COGradeLevel6,
    COGradeLevel7,
    COGradeLevel8,
    COGradeLevel9,
    COGradeLevel10,
    COGradeLevel11,
    COGradeLevel12,
    COGradeLevelPG,
    ExcludeFromCDE,
    COEmpStatusCode,
    COAdminAreaCode,
    COTeachingSubjectCode,
    HourlyTCPreEnc,
    tblCAJobClassID,
    tblCABargainingUnitID,
    Seniority,
    RollIntoID,
    LatestFilled,
    CACountyID,
    tblHREvaluationGroupID,
    EvaluationGroup,
    tblNVHQTCodesID,
    BasedOnID,
    PctOfPos,
    ImputedIncome,
    HasDocs,
    VacancyStatus,
    HQTCode,
    ILLowestGrade,
    ILHighestGrade,
    ILPaidWithTitleI,
    ILTeachAssignment1,
    ILTeachAssignment2,
    ILTeachAssignment3,
    ILTeachAssignment4,
    ILTeachAssignment7,
    ILTeachAssignment6,
    ILTeachAssignment5,
    ILClassesTaught1,
    ILClassesTaught2,
    ILClassesTaught3,
    ILClassesTaught4,
    ILClassesTaught5,
    ILClassesTaught6,
    ILClassesTaught7,
    PosTemplateName,
    tblGLPositionBudgetTemplateID,
    ORExperType,
    ORPositionType,
    NEExcludeFromNSSRS,
    NESalaryType,
    DailyRate,
    PeriodicRate,
    NextYearDailyRate,
    NextYearPeriodicRate,
    tblCAPayMatrixID,
    ZeroPay,
    Expr2,
    NMHD,
    WorkedPeriods,
    PaidPeriods,
    WAS275Adjust,
    WAS275Exclude,
    WAS275Report,
    tblPRWAGradeGroupID,
    BaseRate,
    tblIABEDSPayTypesID,
    tblPRPayCyclesID,
    NMStatus,
    IDDescription,
    MTContractType,
    MTPositionType,
    MTExtraPayType,
    MTTCSReportable,
    MTTeacherDuty,
    CompositeRateFactor,
    ExemptCompositeRate,
    OTFactor,
    WorkCalendarStartDate,
    WorkCalendarEndDate,
    AccountMask,
    SalaryScheduleFullAnnual,
    PARID,
    tblNYERSReportCodesID,
    MTTRSFTE,
    NYERSReportCode,
    LastName,
    FirstName,
    MiddleName,
    GenerationID,
    StateID,
    GATRSPaymentReason,
    GATRSProratedSummerPay,
    GATRSSummerEmploymentPay,
    GAPSERSPaymentReason,
    NVIncludeInContractAmt,
    IDPERSIEarningType,
    FirstPeriodPayAmount,
    tblWYXtraSalReasonsID,
    ILEISExcludeFromEIS,
    ILEISFirstYear,
    ILEISPositionTimeFrame,
    ILEISBilingualLanguage,
    NVPERSStatusCode,
    WAWCPlanID,
    ILEISOverrideFTE,
    ILEISOverrideRCDTS,
    SalarySchedule,
    ExcludeEEOC4,
    SIJobCode,
    WAStateFTE,
    ExcludeFromPAR,
    ACAHrsPerUnit,
    ACAExclude,
    ACAAnnualSalary,
    MAAnnualSalary,
    COPassedHOUSSE,
    COHighlyQualified,
    VTOccupationalTitle,
    MTPayTypeCode,
    NDCertStatus,
    NDSpecEdParaAge,
    NDSpecEdParaInst,
    NDPercentSPEDPK,
    NDPercentKG,
    NDPercent1to6,
    NDPercent7to8,
    NDPercent9to12,
    tblPRPositionsID_Bridge,
    AltHrRate,
    RetControl,
    ReportableDays,
    ReportableHours,
    OEBBReportable,
    GradeLevel,
    PrimaryWorkLocation,
    AZEmpPayType,
    StatusCodeOverride,
    GAPRCInclude,
    AKExcludeFromClassified,
    AKExcludeFromCertified,
    AKESLEndorsement,
    AKSPEDEndorsement,
    AKLowestGrade,
    AKHighestGrade,
    WAFutureBridge,
    COPassedSecondaryTest,
    MAScheduledHours,
    MAAdditionalIncomeReason,
    MANonTaxableReason,
    IAContractDaysOverride,
    LowGradeCode,
    HighGradeCode,
    SpecialEducation,
    DistanceLearning,
    COPassedNCLBHQApproved,
    ApprovedTimeActive,
    ApprovedTimeHours,
    ApprovedTimePeriodLimit,
    ApprovedTimeMaintainHours,
    GACPISubMatterCode,
    GACPIFieldStatus,
    MTWCPlanID,
    AZHQReportable,
    AZHQCore,
    AZHQTeacherOfRecord,
    AZHQPS,
    AZHQKG,
    AZHQG1,
    AZHQG2,
    AZHQG3,
    AZHQG4,
    AZHQG5,
    AZHQG6,
    AZHQG7,
    AZHQG8,
    AZHQG9,
    AZHQG10,
    AZHQG11,
    AZHQG12,
    tblPRHQContentAreaID,
    tblPRHQCriteriaID,
    tblPRHQPositionID,
    tblPRHQStatusLookupID,
    AZHQStartDate,
    AZHQContentArea,
    AZHQCriteria,
    AZHQPosition,
    AZHQStatus,
    AZHQPeriods,
    AZHQSiteNumber,
    AZHQSchoolName,
    AZHQStatusDesc,
    AZHQCriteriaDesc,
    AZHQPositionDesc,
    AZHQContentAreaDesc,
    tblPRHQSchoolsID,
    MEYrlyContractAmt,
    MEPersnlStatusCd,
    MERetPlanStatusCd,
    METimeUnitCd,
    MEExpctdFullTimeWk,
    MEExpctdWeeksYr,
    MEBenPlanCd,
    MERateSchedNo,
    MEEmployerCd,
    MERateOfPay,
    METimePaid,
    MEPosClassCd,
    MEIncludePayRate,
    ExcludeFromTransparency,
    MTRateType
);
'''

insert_viwPREmployees = "insert into viwPREmployees values (" \
    + "?," * 328 + "?)"  # 329 columns


viwPREmployees_data = [
    ('A12M', '27 Emerson Court', 'STONE, RAY ', '369700662',
        'WHITE', 7965, 'ST93229', 'STONE', 'RAY', 'Jay', '1',
        '107 HART RIDGE RD', '', 'PHOENIX', 'AZ', '85085', '9892845829', '1',
        '2', '22', '1983-04-03 00:00:00', '2016-10-24 00:00:00', '',
        '2019-10-24 00:00:00', '', '2016-11-01 00:00:00', '', '', '',
        'DIR OF EDU TECH', '1',
        '16/17 NEW HIRE DIRECTOR OF EDUCATION TECHNOLOGY 10/24/16 BD 10/27/16 EPAR754 ELIGIBLE FOR BENEFITS AND WORK AGREEMENT SALARY PLACEMENT DIRECTOR ',
        '', '', '', '0', '1', '2', '', '0', '1', '', 'False', 'False',
        'Ray.Stone@phxschools.org', 'False', '4', '', '', '', '', '',
        '8', '0', 'False', '2', 'False', '4', '0', '1', 'Administrator',
        'Active', 'Current EE 26', '', '', '1012790', 'No',
        'PHOENIX, AZ 85085', '4', '3', 'April', '3', '12M7.5H (ADM)',
        'Male', 'True', 'WH', 'Officials, Administrators, Managers', '',
        '', '1', 'Yes', '2', '27 Emerson Court', 'C', '1', '384-08-9999',
        'True', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
        '', '', '', '', '', '', '', '', '0', 'jay.stone', 'Married',
        '6854', '26', '0', '0', 'Current EE 26', '0', '26', '26', '2',
        '2011-07-01 00:00:00', '2012-06-30 00:00:00', '4', 'False', '', '',
        '', '', '', '', '', '000', '000', '', '', '', '', '', '', '', '1',
        'Emerson Court', 'True', '17', '0', '0', '0', '0', '0', '', '', '',
        '', '', '', '', '0', '0', '0', '0', '0', '2017-05-11 00:00:00',
        'True', '', '0', '0', 'True', 'False', 'False', '', '', '', '',
        'False', 'False', '0', '0', '0', '0', '0', '', '', '', '0', '', '',
        '', '', '', '', '', '', '', '0', '0', '0', '0', '0', '0', '0', '0',
        'Yes', '0', '', '', '', '', '', '', '', '', '', '', '', '', '', '1',
        '0', '0', '', '1900-01-01 00:00:00', '', '', '', '0', '0', '0', '0',
        '0', 'False', '', '', '', '', 'Not Hispanic or Latino',
        'STONE, RAY  ST93229', '', '0', '0', '0', '0', '0', '0',
        '', '', '0', '0', 'False', 'False', 'True', 'False', '0', '', '',
        'False', 'False', '0', '0', '0', '0', '0', '0', 'False', 'False',
        'RS92817@hotmail.com', '0', 'Ray.STONE@phxschools.org',
        'Work Email Address', '', '', '', '', '', '', '', '', '', '', '',
        '', '', '', '', 'REG - FT - Eligible', '0', '0', '0', '0', '', '',
        'True', '', 'False', 'False', '', '', '12', '', '', '', '', '', '',
        '', '', '', '', '', '', '', '', '', '', '', '', 'True', '', '', '',
        'False', 'False', 'False', '', '', 'False', '', 'False'),
    ('HR', '13 Herrera', 'CLAYTON, BARBARA ASHLEY ', '560255898', 'WHITE',
        7967, 'CL22396', 'CLAYTON', 'BARBARA', 'ASHLEY', '19',
        '554 ELK STREET', '', 'PHOENIX', 'AZ', '85003', '9496080825',
        '1', '2', '12', '1995-05-03 00:00:00', '2016-10-26 00:00:00', '',
        '2016-01-26 00:00:00', '', '', '', '', '', 'PEER IA I', '1',
        '16/17 MIN WAGE INCREASE 1/02/17 EPAR 1241  16/17 SY - NEW HIRE PEER IA GRADE 3/ STEP 1 - EFF: 10/26/2016 - EPAR#692 - BOARD DATE: 11/10/2016',
        '', '', '', '0', '1', '1', '', '0', '1', '', 'False', 'False', '',
        'False', '3', '', '', '', '', '', '11', '0', 'False', '2', 'False',
        '6', '0', '1', 'Class Hourly', 'Active', 'Ineligible', '', '',
        '1013014', 'No', 'PHOENIX, AZ 85003', '5', '3', 'May', '25',
        'CLASSIFIED HOURLY W/ASRS', 'Female', 'True', 'WH', 'Teacher Aides',
        '', '', '1', 'Yes', '14', '13 Herrera', 'C', '1', '999-99-9999',
        'False', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
        '', '', '', '', '', '', '', '', '0', '', 'Single', '6856', '0', '0',
        '0', 'Ineligible for Benefits', '0', '0', '0', '1',
        '2011-07-01 00:00:00', '2012-06-30 00:00:00', '6', 'False', '', '',
        '', '', '', '', '', '000', '000', '', '', '', '', '', '', '', '0.5',
        'Herrera', 'True', '23', '0', '0', '0', '0', '0', '', '', '', '',
        '', '', '', '0', '0', '0', '0', '0', '2017-05-11 00:00:00', 'False',
        '', '0', '0', 'True', 'False', 'False', '', '', '', '', 'False',
        'False', '0', '0', '0', '0', '0', '', '', '', '0', '', '', '', '',
        '', '', '', '', '', '0', '0', '0', '0', '0', '0', '0', '0', 'No',
        '0', '', '', '', '', '', '', '', '', '', '', '', '', '', '0', '0',
        '0', '', '1900-01-01 00:00:00', '', '', '', '0', '0', '0', '0', '0',
        'False', '', '', '', '', 'Hispanic or Latino',
        'CLAYTON, BARBARA ASHLEY  CL22396', '', '0', '0', '0', '0', '0',
        '0', '', '', '0', '0', 'False', 'False', 'True', 'False', '0', '',
        '', 'False', 'False', '0', '0', '0', '0', '0', '0', 'False', 'False',
        'clba2984@gmail.com', '1', 'clba2984@gmail.com',
        'Personal Email Address', '', '', '', '', '', '', '', '', '', '',
        '', '', '', '', '', 'VAR - HRS - Non-Eligible', '0', '0', '0', '0',
        '', '', 'True', '', 'False', 'False', '', '', '9', '', '', '', '',
        '', '', '', '', '', '', '', '', '', '', '', '', '', '', 'True', '',
        '', '', 'False', 'False', 'False', '', '', 'False', '', 'False'),
    ('TEACHER', '04 Dunbar', 'BURGOS, WILLIAM C ', '024620323', 'WHITE',
        7582, 'BU95483', 'WILLIAM', 'WILLIAM', 'C', '7', '2757 JOANNE LANE', '',
        'PHOENIX', 'AZ', '85006', '9785135875', '1', '1', '4',
        '1967-02-08 00:00:00', '2015-03-30 00:00:00', '',
        '2018-07-29 00:00:00', '', '2015-08-01 00:00:00', '', '', '',
        'TEACHER', '3',
        'CANCEL E-PAR 1784 / SUB POSITION TRANSFER FROM TCHR TO DAILY SUB / EFF 05-26-17 / E-PAR 1784 16/17 TRANSFER FROM 4TH GRADE TO 5TH GRADE 7/27/16 NO CHANGE ON LOCATION OR PAY  EPAR 37   15/16 SY-EPAR #374, Transfer from Sub Teacher $153.64 Daily to 4th Grade Teacher at Dunbar BA/$33000.00 + $2000.00 increase= $35000.00, effective 7/29/15, board date 8/13/15.  HIRED AS LTS LOWELL 7/8 SCIENCE / EFF 03-30-15 / BRD DATE 03-26-15 / WITH BENEFITS ',
        '', '', '', '0', '1', '2', '', '0', '3', '', 'False', 'False',
        'william.burgos@phxschools.org', 'False', '2', '', '', '', '', '',
        '27', '0', 'False', '2', 'False', '5', '0', '1', 'Certified',
        'Active', 'Current EE 21', '', '', '108553', 'No',
        'PHOENIX, AZ 85006', '2', '8', 'February', '14', 'TEACHERS', 'Male',
        'True', 'WH', 'Elementary Classroom Teachers', '', '', '3', 'Yes',
        '6', '04 Dunbar', 'C', '1', '999-99-9999', 'True', '', '', '', '', '',
        '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
        '', '0', 'william.burgos', 'Married', '6471', '21', '0', '0',
        'Current EE 21', '0', '21', '21', '4', '2011-07-01 00:00:00',
        '2012-06-30 00:00:00', '5', 'False', '', '', '', '', '', '', '',
        '000', '000', '', '', '', '', '', '', '', '1', 'Dunbar', 'True', '3',
        '0', '0', '0', '0', '0', '', '', '', '', '', '', '', '0', '0', '0',
        '0', '0', '2017-05-11 00:00:00', 'True', '', '0', '0', 'True',
        'False', 'False', '', '', '', '', 'False', 'False', '0', '0', '0',
        '0', '0', '', '', '', '0', '', '', '', '', '', '', '', '', '', '0',
        '0', '0', '0', '0', '0', '0', '0', 'Yes', '0', '', '', '', '', '', '',
        '', '', '', '', '', '', '', '1', '0', '0', '', '1900-01-01 00:00:00',
        '', '', '', '0', '0', '0', '0', '0', 'False', '', '', '', '',
        'Not Hispanic or Latino', 'BURGOS, WILLIAM C  BU95483', '', '0', '0',
        '0', '0', '0', '0', '', '', '0', '0', 'False', 'False', 'True',
        'False', '0', '', '', 'False', 'False', '0', '0', '0', '0', '0', '0',
        'False', 'False', 'hockeyfan92@gmail.com', '1', 'hockeyfan92@gmail.com',
        'Personal Email Address', '', '', '', '', '', '', '', '', '', '', '',
        '', '', '', '', 'REG - FT - Eligible', '0', '0', '0', '0', '', '',
        'True', '', 'False', 'False', '', '', '9', '', '', '', '', '', '', '',
        '', '', '', '', '', '', '', '', '', '', '', 'True', '', '', '',
        'False', 'False', 'False', '', '', 'False', '', 'False'),
]



# It was a lot of work setting up the data for viwPREmployees. Skipping that
# for viwPRPositions.
# insert_viwPRPositions = "insert into viwPRPositions values (" \
#     + "?," * 397 + "?)"  # 398 columns
insert_viwPRPositions = "insert into viwPRPositions (ID) values (9999)"



# I'm wondering why it's better to setup this stuff here instead of the module
# base. seems it would be easier in the base.
def setUpModule():
    # Create sqlite database.
    global db
    global dbc
    global dbfile
    dbfile = "/tmp/tests_visions." + str(time()) + ".db"
    db = sqlite3.connect(dbfile)
    dbc = db.cursor()
    dbc.execute(create_viwPREmployees)
    dbc.executemany(insert_viwPREmployees, viwPREmployees_data)
    dbc.execute(create_viwPRPositions)
    dbc.execute(insert_viwPRPositions)


def tearDownModule():
    # Delete sqlite database.
    dbc.close()
    db.close()
    os.remove(dbfile)


class mconnection():
    "For mocking pyodbc connection objects and returning the sqlite3 objects."

    timeout = None
    autocommit = None
    cstring = None

    # def __init__(self, *args, **kwargs):
    #     pass

    @staticmethod
    def setdecoding(*args, **kwargs):
        pass
    @staticmethod
    def setencoding(*args, **kwargs):
        pass
    @staticmethod
    def cursor():
        return dbc

@patch('api.visions.pyodbc.connect', create=True, return_value=mconnection)
class VisionsRawQuery(TestCase):
    "Test api.visions.exec_sql and dictfetchall, rowfetchall."

    def test_execsql(self, mock):
        # The timeout option isn't actually tested.
        result = api.visions.exec_sql("select ID from viwPRPositions " +
                                      "where ID = 9999", timeout=1)
        result = result.fetchone()[0]
        self.assertEqual(str(result), "9999")

        result = api.visions.exec_sql("select Name, JobTitle, BirthDate " +
                                      "from viwPREmployees where ID = ?", 7965)
        result = result.fetchone()[0]
        self.assertEqual(result, "STONE, RAY ")

    def test_rowfetchall(self, mock):
        result = api.visions.exec_sql("select ID, LastName, FirstName " +
                                      "from viwPREmployees")
        emp = api.visions.rowfetchall(result)
        self.assertEqual(emp, [(7965, 'STONE', 'RAY'),
                               (7967, 'CLAYTON', 'BARBARA'),
                               (7582, 'WILLIAM', 'WILLIAM')])

    def test_dictfetchall(self, mock):
        result = api.visions.exec_sql("select ID, LastName, FirstName " +
                                      "from viwPREmployees " +
                                      "where ID in (7965, 7967)")
        emp = api.visions.dictfetchall(result)
        self.assertEqual(emp, [{'ID': 7965, 'LastName': 'STONE',
                                'FirstName': 'RAY'},
                               {'ID': 7967, 'LastName': 'CLAYTON',
                                'FirstName': 'BARBARA'}])


@patch('api.visions.pyodbc.connect', create=True, return_value=mconnection)
class VisionsSelect(TestCase):
    "Test api.visions.Select."

    def test_select(self, mock):
        query = api.visions.Select("Name, JobTitle, BirthDate", "viwPREmployees",
                                   ID=7965)
        self.assertEqual(query.sql, "select Name, JobTitle, BirthDate from " +
                                    "viwPREmployees where ID = 7965")
        query.execute()
        name = query.cursor.fetchone()[0]
        self.assertEqual(name, "STONE, RAY ")

    def test_select_fetchallrow(self, mock):
        query = api.visions.Select("ID, LastName, FirstName", "viwPREmployees")
        query.execute()
        emp = query.fetch_all_row()
        self.assertEqual(emp, [(7965, 'STONE', 'RAY'),
                               (7967, 'CLAYTON', 'BARBARA'),
                               (7582, 'WILLIAM', 'WILLIAM')])

    def test_select_fetchvalue(self, mock):
        query = api.visions.Select("Name", "viwPREmployees", "ID=7965")
        name = query.fetch_value()
        self.assertEqual(name, "STONE, RAY ")


@patch('api.visions.pyodbc.connect', create=True, return_value=mconnection)
class VisionsViwpremployees(TestCase):
    "Test Viwpremployees class."

    def test_asdf(self, mock):
        name = api.visions.Viwpremployees().Name(7965)
        self.assertEqual(name, "STONE, RAY ")