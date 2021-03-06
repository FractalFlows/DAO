# Big thanks to @colm from our slack chat for thinking of this attack !!!
scenario_description = (
    "Before commit 842ce13aedca6365d1f6f4b62c215d4e9b265ffa an attacker could "
    "create a proposal with a huge deposit. Then he could create a split DAO "
    "proposal to get his share of ether plus his share of the deposit he gave."
    " Then if the original proposal meets the quorum the attacker will also "
    "get his deposit back."
)


def run(ctx):
    ctx.assert_scenario_ran('fund')

    ctx.create_js_file(substitutions={
        "dao_abi": ctx.dao_abi,
        "dao_address": ctx.dao_addr,
        "offer_address": ctx.offer_addr,
        "attack_debating_period": ctx.args.colmattack_attack_debate_secs,
        "split_debating_period": ctx.args.colmattack_split_debate_secs,
        "attack_deposit": ctx.args.colmattack_attack_deposit,
        "attack_proposal_id": ctx.next_proposal_id()
    })

    ctx.execute(expected={
        "final_diff": 0,  # should be 0, the attacker MUST NOT make any profit
        "split_dao_total_supply": float(ctx.token_amounts[2])
    })
