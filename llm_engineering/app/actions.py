from llm_engineering.models import GeminiClient, create_word_explanation, create_questions, create_answers, create_new_questions, create_summary_adjustment
from llm_engineering.infrastructure import clean_wiki_content



class PabloAI:
    def __init__(self):
        # Starting PabloAI'
        pass

    def makeSummary(self, keyword: str, data: str) -> dict:
        print("Making Initial Explanation ...")
        
        # Test GeminiClient import
        gemini_client = GeminiClient()
        print("✓ GeminiClient imported successfully")
        
        # Test get_data and create_initial_summary
        cleaned_data = clean_wiki_content(data)
        print("✓ data imported and cleaned successfully")   
        
        # Test create_word_explanation
        explanation = create_word_explanation(keyword, cleaned_data)

        print("✓ create_word_explanation imported and called successfully")
        print("\nExplanation:")
        print(explanation)
        
        split_explanation = explanation.split("\n")         
       
        gemini_client.close()

        results = {
            "cleaned_data": cleaned_data,
            "general_explanation": split_explanation[0],
            "detailed_explanation": split_explanation[1]
        }
        
        return results

    def makeQuestions(self, keyword: str, explanation: str) -> dict:
        print("Making Initial Questions ...")

        gemini_client = GeminiClient()
        print("✓ GeminiClient imported successfully")

        questions = create_questions(keyword, explanation)
        print("✓ create_questions imported and called successfully")
        print("\nQuestions:")
        print(questions)

        answers = create_answers(questions)
        print("✓ create_answers imported and called successfully")
        print("\nAnswers:")
        print(answers)

        gemini_client.close()

        results = {
            "questions_raw": questions,
            "answers_raw": answers
        }

        return results

    def makeSummaryAdjustment(self, keyword: str, new_questions: str, new_answers: str) -> dict:
        print("Making Summary Adjustment ...")

        GeminiClient()
        print("✓ GeminiClient imported successfully")  

        summary_adjustment = create_summary_adjustment(keyword, new_questions, new_answers)
        print("✓ create_summary_adjustment imported and called successfully")
        print("\nSummary Adjustment:")
        print(summary_adjustment)

        results = {
            "summary_adjustment": summary_adjustment
        }

        return results    

    def makeNewQuestions(self, keyword: str, data: str, wrong_questions: str) -> dict:
        print("Making New Questions ...")

        gemini_client = GeminiClient()
        print("✓ GeminiClient imported successfully")

        cleaned_data = clean_wiki_content(data)
        print("✓ data imported and cleaned successfully")

        new_questions = create_new_questions(keyword, cleaned_data, wrong_questions)
        print("✓ create_new_questions imported and called successfully")
        print("\nNew Questions:")
        print(new_questions)

        new_answers = create_answers(new_questions)
        print("✓ create_answers imported and called successfully")
        print("\nAnswers:")
        print(new_answers)

        gemini_client.close()

        results = {
            "new_questions": new_questions,
            "new_answers": new_answers
        }

        return results
    