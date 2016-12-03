import ner
import traceback

# tagger = ner.HttpNER(host='127.0.0.1', port=9191)
tagger = ner.SocketNER(host='127.0.0.1', port=9191)
tagger.oformat="inlineXML"


print(tagger.oformat)
# print(tagger.classifier)
# print(tagger.spacing)

# print(tagger.tag_text("University Singapore"))
# print(tagger.tag_text("I lived in Singapore"))
# print(tagger.tag_text("I graduated from University of Singapore on 1999"))
# print(tagger.tag_text("University of Arizona"))
# print(tagger.tag_text("Intel"))
# print(tagger.tag_text("Apple"))
# print(tagger.tag_text("Thomas"))
# print(tagger.tag_text("Tuesday"))
# print(tagger.tag_text("I complained to Microsoft Bill Gates and they told me to see the mayor of New York"))

print(tagger.tag_text("""
<html>
    <head>
    </head>
    <body>
        <div class="vcard single_form-content" id="resume_body">
            <div class="last basicInfo-content" id="basic_info_row">
                <div class="data_display" id="basic_info_cell">
                    <h1 class="fn " id="resume-contact" itemprop="name">
                        Eldeniya Gedara Dharmakeerthy
                    </h1>
                    <h2 id="headline" itemprop="jobTitle">
                        APPLICATION FOR A SENIOR MANAGEMENT POST
                    </h2>
                    <div id="contact_info_container">
                        <div class="adr" itemprop="address" itemscope="" itemtype="http://schema.org/PostalAddress">
                            <p class="locality" id="headline_location" itemprop="addressLocality">
                                Athurugiriya
                            </p>
                        </div>
                        <div class="separator-hyphen">
                            -
                        </div>
                    </div>
                </div>
            </div>
            <div class="section-item workExperience-content">
                <div>
                    <div class="section_title">
                        <h2>
                            Work Experience
                        </h2>
                    </div>
                </div>
                <div class="items-container" id="work-experience-items">
                    <div class="work-experience-section last" id="workExperience-EeRDmvR8Ub-XCpTgI3RMKQ">
                        <div class="data_display">
                            <p class="work_title title">
                                Professional researcher
                            </p>
                            <div class="work_company">
                                <span class="bold">
                                    National Science Foundation Sri Lanka
                                </span>
                                <div class="separator-hyphen">
                                    -
                                </div>
                                <div class="inline-block">
                                    <span>
                                        Colombo
                                    </span>
                                </div>
                            </div>
                            <p class="work_description">
                                More than 35 years experience in electronics and telecom inSri lanka and abroad Last position held 'senior manager/Lead consultant planning and
development-Dialog Telecom
                                <br/>
                                Presently retired and doing part time lecturing at Post Graduate institute of business Management
                                <br/>
                                I am presently reading for my PhD9 research based) Thesis completed and awaiting convocation offered by international university of America-London
                                <br/>
                                <br/>
                                I am fluent in advanced research methodologies qualitative and Quantitative
                                <br/>
                                Awaiting a full time academic career I hope Data I have provided is enough for your perusal my contact telephone number […]
                                <br/>
                                Thank you,
                                <br/>
                                yours truly E.G.dharmakeerthy
                            </p>
                        </div>
                    </div>
                </div>
            </div>
            <div class="section-item education-content">
                <div>
                    <div class="section_title">
                        <h2>
                            Education
                        </h2>
                    </div>
                </div>
                <div class="items-container" id="education-items">
                    <div class="education-section last" id="education-EeWHYC4Lv4ibppTgI3RMKQ">
                        <div class="data_display" itemprop="alumniOf" itemscope="" itemtype="http://schema.org/EducationalOrganization">
                            <p class="edu_title">
                                PhD in mobile communications and society
                            </p>
                            <div class="edu_school">
                                <span class="bold" itemprop="name">
                                    international university of america - London
                                </span>
                                -
                                <div class="inline-block" itemprop="address" itemscope="" itemtype="http://schema.org/PostalAddress">
                                    <span itemprop="addressLocality">
                                        London
                                    </span>
                                </div>
                            </div>
                            <p class="edu_dates">
                                2009 to 2014
                            </p>
                        </div>
                    </div>
                </div>
            </div>
            <div class="section-item skills-content">
                <div>
                    <div class="section_title">
                        <h2>
                            Skills
                        </h2>
                    </div>
                </div>
                <div class="items-container" id="skills-items">
                    <div class="data_display">
                        <div class="skill-container resume-element">
                            <span class="skill-text">
                                Project Management
                            </span>
                        </div>
                    </div>
                </div>
            </div>
            <div class="section-item additionalInfo-content">
                <div>
                    <div class="section_title">
                        <h2>
                            Additional Information
                        </h2>
                    </div>
                </div>
                <div class="items-container" id="additionalinfo-items">
                    <div class="last" id="additionalinfo-section">
                        <div class="data_display">
                            <p>
                                i am having expertise on Satellite communications
                            </p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </body>
</html>

"""))

# tagger.get_entities("University of California is located in California, United States")
# tagger.json_entities("Alice went to the Museum of Natural History.")

