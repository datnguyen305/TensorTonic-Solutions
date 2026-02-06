import math
def evaluate_shadow(production_log, shadow_log, criteria):
    """
    Evaluate whether a shadow model is ready for promotion.
    """
    prod_len = len(production_log)
    shad_len = len(shadow_log)
    min_accuracy_gain = criteria['min_accuracy_gain']
    max_latency_p95 = criteria['max_latency_p95']
    min_agreement_rate = criteria['min_agreement_rate']
    product_count_matching = 0 
    actual_count_matching = 0

    #accuracy_gain
    for i in range(prod_len):
        if production_log[i]['prediction'] == production_log[i]['actual']:
            product_count_matching += 1
        if shadow_log[i]['prediction'] == shadow_log[i]['actual']:
            actual_count_matching += 1 
    prod_acc = product_count_matching/prod_len
    shadow_acc = actual_count_matching/shad_len
    accuracy_gain = shadow_acc - prod_acc

    #shadow_latency
    shadow_latent_list=[]
    for i in range(shad_len):
        shadow_latent_list.append(shadow_log[i]['latency_ms'])
    srt_latent = sorted(shadow_latent_list)
    index = math.ceil(0.95*shad_len) - 1 
    shadow_latency = srt_latent[index]

    #agreement_rate
    agreement_inputs = 0 
    for i in range(prod_len):
        if production_log[i]['prediction'] == shadow_log[i]['prediction']:
            agreement_inputs += 1
    agreement_rate = agreement_inputs/prod_len

    promote = False 

    if accuracy_gain >= criteria['min_accuracy_gain'] and shadow_latency <= criteria['max_latency_p95'] and agreement_rate >= criteria['min_agreement_rate']:
        promote = True
    
    result = {
        "promote": promote,
        "metrics":{
            "shadow_accuracy": shadow_acc,
            "production_accuracy": prod_acc,
            "accuracy_gain": accuracy_gain,
            "shadow_latency_p95": shadow_latency,
            "agreement_rate": agreement_rate
        }
    }

    return result




    

        