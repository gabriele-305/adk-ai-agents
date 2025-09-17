from google.adk.agents import Agent
from datetime import datetime
from google.adk.tools import ToolContext

def get_current_time() -> dict:
    """Get the current time in the format YYYY-MM-DD HH:MM:SS"""
    return {
        "current_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }

def refund_course(tool_context: ToolContext) -> dict:
    """
    Simulating refunding the AI Marketing Platform course.
    Updates the state by removing the course from purchased_courses.
    """
    course_id = "ai_marketing_platform"
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    current_purchased_course = tool_context.state.get("purchased_courses", [])

    courses_id = [
        course["id"] for course in current_purchased_course if isinstance(course, dict)
    ]
    if course_id not in courses_id:
        return {
            "status": "error",
            "message": "You don't own this course, so it can't be refunded.",
        }
    
    new_purchased_courses = []
    for course in current_purchased_course:
        if not course or not isinstance(course, dict):
            continue
        if course["id"] == course_id:
            continue
        new_purchased_courses.append(course)

    tool_context.state["purchased_courses"] = new_purchased_courses

    current_interaction_history = tool_context.state.get("interaction_history", [])
    new_interaction_history = current_interaction_history.copy()
    new_interaction_history.append({
        "action": "refund_course", "course_id": course_id, "timestamp": current_time
    })
    tool_context.state["interaction_history"] = new_interaction_history

    return {
        "status": "success",
        "message": """Successfully refunded the AI Marketing Platform course! 
         Your $149 will be returned to your original payment method within 3-5 business days.""",
        "course_id": course_id,
        "timestamp": current_time,
    }

order_agent = Agent(
    name="order_agent",
    model="gemini-2.0-flash",
    description="Order agent fot viewing purchase history and processing refunds",
    instruction="""
    You are the order agent for the AI Developer Accelerator community.
    Your role is to help users view their purchase history, course access and process refunds.

    <user_info>
    Name: {user_name}
    </user_info>

    <purchase_info>
    Purchased Courses: {purchased_courses}
    </purchase_info>

    <interaction_history>
    {interaction_history}
    </interaction_history>

    When user ask about their purchase:
    1. Check their course list from the purchase info above
        - Course information is stored as an object with "id" and "purchase_date" properties
    2. Format the response clearly showing:
        - Which course they own
        - When they were purchased (from the course.purchase_date property)
    
    When users request a refund:
    1. Verify they own the course they want to refund ("ai_marketig_platform")
    2. If they own it:
        - Use the refund_course tool to process the refund
        - Confirm the refund was successfull
        - Remind them the money will be returned to their original payment method
        - If it's been more then 30 days, inform them that they are not eligible for a refund
    3. If they don't own it:
        - Inform them they don't own the course, so no refund is needed

    Course Information:
    - ai_marketing_platform: Fullstack AI Marketing Platform ($149)

    Example Response for Purchase History:
    "I've processed your refund for the Fullstack AI Marketing Platform course.
    Your $149 will be returned to your original payment method within 3-5 business days.
    The course has been removed from your account."

    If they haven't purchased any courses:
    - Let them know that they don't have any courses yet
    - Suggest talking to the sales agent about the AI Marketing Platform course

    REMEMBER:
    - Be clear and professional
    - Mention our 30-day money-back guarantee if relevant
    - Direct course content question to course support
    - Direct purchase inquiries to sales
    """,
    tools=[get_current_time, refund_course]
)