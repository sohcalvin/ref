import nltk


doc = """Java, Python, pattern recognition
You will lead the design and execution of datax analytics projects by taking ownership of the full datax analytics lifecycle iterations - from formulating business questions, datax gathering, cleansing and transforming datax, conducting exploratory datax analysis, assessing, building and validating models to interpreting and communicating results. You will engage the key stakeholders to understand the business issues and opportunities, and formulate it in a manner that can be analyzed and modeled. You will solicit and prepare datax from the relevant sources, ensuring that high standards of datax quality and integrity are maintained and documented. You will select suitable statistical techniques and analytics methodologies that best meet the analytics objectives and utilize analytical tools to perform statistical and analytic activities to develop models that are robust and reliable. You will translate the analytical results into actionable insights and will collaborate with IT and functional teams to implement the analytical models into ongoing business processes. You will track the model quality and post implementation metrics, and intervene promptly to ensure the model's continued relevance and reliability for decision-making. You will establish and maintain datax and analytics standards and define and maintain the datax analytics standards and processes to improve the datax analytics capabilities in the Bank. You will support ad-hoc analytics and reporting requests, as well as engage stakeholders to understand business requirements and acquire datax from existing applications and datax sources. Pre-requisites: Bachelor or Master degree in Applied Statistics, Data Science and/ or Business Analytics At least 5 years of hands-on experience in datax analytics, preferably in a private banking environment with a proven track record of engaging the senior management; as well as leading and implementing successful datax analytics projects Proven experience in the application of exploratory datax analysis, supervised and unsupervised learning, statistical modeling and visualization techniques Expert practitioner in R software packages for datax and exploratory analysis, modeling and visualization - this is a mandatory requirement; knowledge of SQL is a plus Proficient in Microsoft Office and SharePoint collaboration tools Possess excellent verbal and written communication skills - in particular having the ability to understand business problems precisely and able to summarize expectations clearly; translate and present complex analytical results to the business decision makers clearly by using terms are easily understood Possess strong problem solving skills and interpersonal skills Submit your application to recruitment@wmrc.com.sg quoting the Job Title or call +65 6549 7818 for more information. Your interest will be treated in strict confidence. Data collected will be used for recruitment purposes only. Personal datax provided will be used strictly in accordance with the relevant datax protection law and WMRC's personal information and privacy policy.
"""

def launchChunkParserGUI():
    nltk.app.chunkparser()

def describePOS() :
    nltk.help.upenn_tagset()

# returns a list of array containing list<token, POS_value>
def performPos(document):
    sentences = nltk.sent_tokenize(document)
    sentences = [nltk.word_tokenize(sent) for sent in sentences]
    sentences = [nltk.pos_tag(sent) for sent in sentences]
    return sentences

def chunkPosResult(posResult, grammar) :
    cp = nltk.RegexpParser(grammar)
    outTokens = []
    for s in posResult :
        chunked = cp.parse(s)
        for node in chunked :
            if type(node) is nltk.Tree:
                if(node.label() == "NP") :
                    leaves = node.leaves()
                    unPos = [ i for i,j in leaves]
                    outTokens.append(' '.join(unPos))
                    # print(leaves)
                    # print(">>", ' '.join(unPos))
    return outTokens




# describePOS()
result = performPos(doc)

grammar="NP: {<NN|NNP|NNPS|NNS><NN|NNP|NNPS|NNS>?}"
chunkedResult = chunkPosResult(result, grammar)
print(chunkedResult)



    # nouns = [ (i,j) for i,j in s if j.startswith("NN") ]
    # print(nouns)


# grammar = "NP: {<DT>?<JJ>*<NN>}"
# grammar = "NP: {<NN>?<NN>+|<DT>?<JJ>*<NN>}"
# grammar = r"""
#   NP: {<DT|PP\$>?<JJ>*<NN>}   # chunk determiner/possessive, adjectives and noun
#       {<NNP>+}                # chunk sequences of proper nouns
#       {<NN>+}
# """


# chunked = cp.parse(result[1])
# print(chunked)
