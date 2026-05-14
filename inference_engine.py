from laptops import laptops

def recommend_laptop(processing, graphics, portability, budget):

    recommendations = []
    reasons = []

    # Forward chaining rules

    if processing >= 4 and graphics >= 4:
        reasons.append("High processing and graphics requirements detected")

        for laptop in laptops:
            if laptop["performance_level"] >= 4:
                recommendations.append(laptop)

    elif portability >= 4:
        reasons.append("High portability preference detected")

        for laptop in laptops:
            if laptop["portability"] >= 4:
                recommendations.append(laptop)

    return recommendations, reasons