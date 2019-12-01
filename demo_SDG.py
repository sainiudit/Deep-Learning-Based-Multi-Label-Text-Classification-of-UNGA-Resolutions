from core import GoalTargetInterface

goal_threshold=0.6
target_threshold=0.6

model_options = {
	'tf_model':'USE_DAN',
	'concat_target_definitions':True,
	'with_semantic_shifting':True,
	'with_topic_scaling':True,
	'with_document_log_length_scaling':True,
	'with_stemmed_tfidf':True,
	'with_centered_similarity':True,
	'with_tfidf_similarity':True,
	'cache_queries':False,
	'log':False
}

# Build similarity queries. Our goal is to know how similar is the query to the corpus
queries = [
	u"He is hungry and needs nutrition, they need to help him.",
	u"the third and the second ship arriving from Moscow. That's for the SDG 4. He is hungry and needs nutrition, they need to help him.",
	u"We are going to tackle the Sustainable Development Goal 7.",
	u"We are going to tackle the seventh Sustainable Development Goal.",
	u"there many different countries trying to work together on something",
	u"sdg 4",
	u"4",
	u"hello everyone there something new to discuss, 4 new topics indeed",
	u"There are 17 Sustainable Development Goals.",
	u"resolution 70/1 of 25 September 2015, entitled “Transforming our world: the 2030 Agenda for Sustainable Development”, in which it adopted a comprehensive, far-reaching and people-centred set of universal and transformative 17 Sustainable Development Goals and targets, its commitment to working tirelessly for the full implementation of the Agenda by 2030, its recognition that eradicating poverty in all its forms and dimensions, including extreme poverty, is the greatest global challenge and an indispensable requirement for sustainable development, its commitment to achieving sustainable development in its three dimensions — economic, social and environmental — in a balanced and integrated manner, and to building upon the achievements of the Millennium Development Goals and seeking to address their unfinished business,",
	u"The 17 Sustainable Development Goals and 169 targets which we are announcing today demonstrate the scale and ambition of this new universal Agenda. They seek to build on the Millennium Development Goals and complete what they did not achieve. They seek to realize the human rights of all and to achieve gender equality and the empowerment of all women and girls. They are integrated and indivisible and balance the three dimensions of sustainable development: the economic, social and environmental.",
	u"*Notes with appreciation* that the preparatory process and the high-level segment of UNISPACE+50 resulted in documents aimed at articulating a comprehensive, inclusive and strategically oriented vision on strengthening international cooperation in the exploration and peaceful uses of outer space, in which space is seen as a major driver of and contributor to the achievement of the Sustainable Development Goals2 for the benefit of all countries;",
	u"*Noting* that, while considerable progress has been made over the past decade across all areas of development, the pace of progress observed in recent years is insufficient and uneven to fully meet the Sustainable Development Goals and targets by 2030, especially in the area of rural poverty eradication, ",
	u"*Reaffirms* that eradicating poverty in all its forms and dimensions, including extreme poverty, for all people everywhere, is the greatest global challenge and an indispensable requirement for sustainable development, as well as an overarching objective of the 2030 Agenda for Sustainable Development, of which the Addis Ababa Action Agenda of the Third International Conference on Financing for Development is an integral part, supporting and complementing it; ",
	u"*Recognizes* the importance of addressing the diverse needs of and challenges faced by countries in special situations, in particular African countries, the least developed countries, landlocked developing countries and small island developing States, as well as the specific challenges facing many middle-income countries, and therefore requests the United Nations development system, the international financial institutions, regional organizations and other stakeholders to ensure that these diverse and specific development needs are appropriately considered and addressed, in a tailored fashion, in their relevant strategies and policies, with a view to promoting a coherent and comprehensive approach towards individual countries; ",
	u"*Strongly regretting *the decision of the Government of Myanmar to discontinue cooperation with the Special Rapporteur of the Human Rights Council on the situation of human rights in Myanmar and to deny her access to Myanmar since January 2018, and calling upon the Government of Myanmar to resume its cooperation with the Special Rapporteur without delay,",
	u"*Acknowledging with grave concern* statements made by the Secretary-General on 26 February 2018, the United Nations High Commissioner for Human Rights on 7 March 2018, the Assistant Secretary-General for Human Rights on 6 March 2018 and the Secretary-General of the Organization of Islamic Cooperation on 27 February 2018 on the situation of human rights in Rakhine State, in which they referred to ethnic cleansing in Myanmar, and recalling the resolution adopted by the Council of Foreign Ministers of the Organization of Islamic Cooperation at its forty-fifth session on the establishment of an Organization of Islamic Cooperation ad hoc ministerial committee on accountability for human rights violations against the Rohingya and the recommendations made by the participants in the international consultation meeting on the Rohingya crisis, which was held in Ankara on 6 July 2018,",
	u"*Also approves* the establishment of seven posts (4 P5, 1 P4 and 2 P3), effective 1 January 2019, under section 18A, Economic and social development in Africa, of the programme budget for the biennium 2018-2019; ",
	u"*Recalls* paragraphs 19, 20 and 22 (c) of the report of the Advisory Committee, and requests the Secretary-General to continue to analyse the options concerning the long-term arrangements for the Residual Special Court in greater detail by identifying possible savings and additional measures on transparency, accountability and cost efficiency of the use of the commitment authority, and to report thereon to the General Assembly at the main part of its seventy-fourth session; ",
	u"*Recalling* section I of its resolution 68/247 B of 9 April 2014, section I of its resolution 69/274 A of 2 April 2015, section IV of its resolution 70/248 A, section II of its resolution 71/272 A and section IX of its resolution 72/262 A, ",
	u"(b)Welcomes that nationallevel analysis will be inputs for regional consultations on volunteering in 2019, and requests that these regional consultations be held under the auspices of the regional commissions of the United Nations in the context of the regional forums on sustainable development, providing an opportunity for Member States and partners to discuss evidence and approaches, identify opportunities for addressing knowledge gaps and ensure, among other things, that national and regional inputs into the high-level political forum on sustainable development take account of volunteer contributions to the 2030 Agenda; ",
	u"*Recalls* paragraph 24 of the report of the Secretary-General on the pattern of conferences, also recalls that, in paragraph 81 of its resolution 56/253 of 24 December 2001, it requested the Secretary-General to ensure that conference services were managed in an integrated manner throughout all duty stations in the Organization, stresses again that the Department for General Assembly and Conference Management is responsible for the implementation of policy, the formulation of standards and guidelines, overseeing and coordinating United Nations conference services and the overall management of resources under the relevant budget section, while the United Nations Offices at Geneva, Vienna and Nairobi remain responsible and accountable for day-to-day operational activities, as indicated in section II.B, paragraph 7, of its resolution 57/283 B;",
	u"*Notes* the completion of the internal reviews concerning accountability mechanisms and the clear delineation of responsibility between the Under-Secretary-General for General Assembly and Conference Management and the Directors-General of the United Nations Offices at Geneva, Nairobi and Vienna for conference management policies, operations and resource utilization, requests the Secretary-General to report on the outcome of the internal reviews to the General Assembly at its seventy-fourth session, and in this regard recalls, inter alia, paragraph 36 of its resolution 72/19; ",
	u"*Requests* the Secretary-General to continue to ensure that measures taken by the Department for General Assembly and Conference Management to seek the evaluation by Member States of the quality of the conference services provided to them, as a key performance indicator of the Department, provide equal opportunities to Member States to present their evaluations in the six official languages of the United Nations and are in full compliance with relevant resolutions of the General Assembly, and also requests the Secretary-General to report to the Assembly, through the Committee on Conferences, on progress made in this regard; ",
	u"*Recalls* paragraph 28 of its resolution 72/266 B, and requests the Secretary-General to include in his review the human resources functions, including an assessment of progress achieved towards equitable geographical representation, bearing in mind Article 101, paragraph 3, of the Charter of the United Nations.",
	u"*Invites* Member States and relevant United Nations entities, international and regional organizations, the institutes of the United Nations crime prevention and criminal justice programme network and other relevant stakeholders to provide the Commission, through its secretariat, for consideration during its twenty-eighth session, views on how the Commission can contribute to the review of the implementation of the 2030 Agenda for Sustainable Development, in particular Sustainable Development Goal 16, and requests the Secretariat to also bring that information to the attention of the high-level political forum at its meeting in 2019 and the Fourteenth United Nations Congress on Crime Prevention and Criminal Justice, within existing reporting requirements.",
	u"*Reaffirming* its previous resolutions on the situation of human rights in Myanmar, the most recent of which being resolution 72/248 of 24 December 2017, and recalling the resolutions and decisions of the Human Rights Council, the most recent of which being resolutions 39/2 of 27 September 2018, 37/32 of 23 March 2018 and S27/1 of 5 December 2017, and the statement by the President of the Security Council issued on 6 November 2017,",
	u"Having considered the report of the Secretary-General and the related report of the Advisory Committee on Administrative and Budgetary Questions, ",
	u"Oris V. Wells said nonsenses.",
	u"Notes with appreciation that, at its forty-third session, held in Nairobi from 11 to 13 April 2016, the Intergovernmental Panel on Climate Change decided to prepare a special report on climate change and oceans and the cryosphere;",
	u"Recognizes that the implementation of the Beijing Declaration and Platform for Action and the fulfilment of the obligations of States parties under the Convention on the Elimination of All Forms of Discrimination against Women are mutually reinforcing in respect of achieving gender equality and the empowerment of women, and welcomes in this regard the contributions of the Committee on the Elimination of Discrimination against Women to promoting the implementation of the Platform for Action and the outcome of the twenty-third special session;",
	u"Expressing concern that women and girls with disabilities are subject to multiple and intersecting forms of discrimination, which limit their enjoyment of all human rights and fundamental freedoms on an equal basis with others, particularly with regard to the equal access of persons with disabilities to education and employment, access to health-care services, including for sexual and reproductive health, access to justice and equal recognition before the law, the ability to participate in political and public life, live independently and be included in the community and have the freedom to make their own choices,",
	u"Promote meaningful civil society engagement to encourage Governments to develop ambitious national multisectoral responses for the prevention and control of non-communicable diseases, and to contribute to their implementation, forge multistakeholder partnerships and alliances that mobilize and share knowledge, assess progress, provide services and amplify the voices of and raise awareness about people living with and affected by non-communicable diseases;",
	u"Expresses its deep concern, in this regard, about the negative impact on the realization of the right to development owing to the further aggravation of the economic and social situation, in particular of developing countries, as a result of the ongoing international energy, food and financial crises, as well as the increasing challenges posed by global climate change and the loss of biodiversity, which have increased vulnerabilities and inequalities and have adversely affected development gains, in particular in developing countries;",
	u"Encourages States that have not yet integrated children's issues into their overall rule of law efforts to do so and to develop and implement a comprehensive and coordinated juvenile justice policy to prevent and address juvenile delinquency and to address risks and causes for children's contact with the juvenile and/or criminal justice system, as well as with a view to promoting, inter alia, the use of alternative measures, such as diversion and restorative justice, and complying with the principle that deprivation of liberty of children should be used only as a measure of last resort and for the shortest appropriate period of time, as well as to avoid, wherever possible, the use of pretrial detention for children;",
	u"Recalling implementation target 2.c under Sustainable Development Goal 2 of the 2030 Agenda for Sustainable Development, the aim of which is to adopt measures to ensure the proper functioning of food commodity markets and their derivatives and to facilitate timely access to market information, including on food reserves, in order to help to limit extreme food price volatility, and implementation target 9.b under Goal 9 of the 2030 Agenda, the aim of which is to support domestic technology development, research and innovation in developing countries, including by ensuring a conducive policy environment for, inter alia, industrial diversification and value addition to commodities,",
]

interface = GoalTargetInterface(goal_options=model_options, target_options=model_options)
interface.model.cache_docvecs(queries)

# Find queries similarity
for index,query in enumerate(queries):
	print('----------------------------------------')
	print('Query', index+1)
	print('Content: "{}"\n'.format(query))
# Get the SDG
	result_list = interface.get_goal_and_target(query, goal_threshold=goal_threshold, target_threshold=target_threshold)
	for sdg, target_list in result_list:
		sdg = {'id':sdg['id'], 'confidence':sdg['similarity']}
		target_list = [
			{'id':t['id'], 'confidence':t['similarity']}
			for t in target_list
		]
		print(f'SDG: {sdg}, Target list: {target_list}')

print('----------------------------------------')
