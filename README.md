# Logistic-Regression-What-affect-the-odds-of-Covid-19-mortality
Logistic Regression What affect the odds of Covid-19 mortality

## 1. Research motivation and methodology

This report uses logistic regression (LR) and various related-indicators as independent variable to investigate mortal possibilities of people who have taken the test of carrying Covid-19 virus during the epidemic period. The study initially identifies and examines nine indicators (represented by eighteen predicter variables) that can classify people whether is “alive” or “dead”. This study unavoidably biased the Covid-19 mortality rate because there are neglected or under-served segments of the population who are less likely to access healthcare or testing. Under-detection of cases may be exacerbated during an epidemic, when testing capacity may be limited and restricted to people with severe cases and priority risk groups (such as frontline healthcare workers, elderly people and people with comorbidities).

## 2. Dataset

Dataset Link: https://data.cdc.gov/Case-Surveillance/COVID-19-Case-Surveillance-Public-Use-Data/vbim-akqf

The data is provided by CDC Case Surveillance Task Force [3]. The study sample consists of over five million country-level deidentified patient cases from beginning of the outbreak to Nov. 24, 2020 in US only. The dataset includes 11 data element public as columns and each row is a deidentified patient and is updated monthly. The columns cdc_report_dt which represents for initial case report date to CDC and pos_spec_dt which represents for date of first positive specimen collection are disregarded in our regression model. The reason is that at the start of the outbreak, detected cases are more likely to be severe or fatal.
Patients with severe illness are more likely to present at health facilities and to be confirmed by laboratory test. Therefore, at beginning of pandemic the mortality rate is much higher. If we put the columns of initial time report date and date of first positive specimen collection into the regression model, the result is always biased because there is potential bias in detections of cases and deaths.
Then we use the remaining 8 columns as initial input of the regression model. After we remove missing and unknown values for sex, hospitalization status, ICU admission status, Death status, and Presence of underlying comorbidity for, the remaining 411 thousand of samples will be used for this research propose. Moreover, if symptom onset date is later than the CDC report date, this deidentified patient is considered asymptomatic carrier. So, our team created a new column called asymptomatic, yes if the patient is an asymptomatic carrier, no if symptomatic.

## 3. EDA

In addition to data cleansing and to create initial hypothesis of our model, our team conducts some initial statistics analysis of the data. The data consist of 395399 laboratory-confirmed case and 16463 probable case; the data collects the number of 216852 females and the number of 195010 males. There are 29543 cases use ICU, which is 7.17% of total cases, and 217607 cases presence of underlying comorbidity or disease, which is 52.83% of total cases. The majority ethnicity of the data is white, the second ethnicity group is Hispanic and Latino, then black, and last Asian.
Moreover, among 411862 rows of data, the number of 80810 cases received hospitalization service, which roughly equal to 19.62% of total cases. By given the number of death cases, there are the number of 26381 death cases received hospitalization service, and 3798 death cases never receive hospitalization. Intuitively, it seems that hospitalization would increase the odds of death. However, the correlation between hospitalization and death cannot simply demonstrate the causal effect. There are some error terms that do not include in the model may have effect on both hospitalization and death. For example, if a patient identified as severe cases, it might cause he or she receives hospitalization service and death.
Accordingly, our team assumes that there are 3798 cases that died because that they never receive hospitalization service.

## 4. Regression Model

Based on the intuition, our initial hypothesis is that there is a logistic relationship between the predictor variables and the log-odds of the event that response variable Y=1, which means being “dead”. The ultimate goal is to not only observe the effect of X on Y but also find the most important factors for Covid-19 mortality. For example, it is possible to decrease the country-level related Covid-19 mortality by arranging hospitals’ bed and ICU resources. Since some predictor variables are categorical variable, we need to create dummy variable to replace them.
\
\
You can find the model mathematical form in the report.

## 5. Conclusion

In this model we try to figure out if certain characteristic of a patient will cause a higher mortality and then the result is able to assist hospitals make medical resources arrangement and facilitate the US government to designate the ‘biased’ healthcare policy for saving patients who are likely to be survive if they can get corresponding and on-time treatment. For instance, the regression shows that Asian American is associated with 13.93% increases in odds of COVID-19 mortality. If we put the income conditions of different ethnicity into considerations, it is obvious that ethnicity with low-income are more likely to die. A possible explanation is that some poor Asian American cannot afford health insurance. The government can buy the special health insurance designed for epidemic for those citizens to save life.
