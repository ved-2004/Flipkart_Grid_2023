from aiohttp import ClientSession, ClientError
from json import loads, JSONDecodeError


class Completion:
    """
    This class provides methods for generating completions based on prompts.
    """

    async def create(self, prompt):
        """
        Create a new completion based on the given prompt.

        Args:
            prompt (str): The prompt to generate a completion for.

        Returns:
            str: The generated completion.

        Raises:
            Exception: If unable to fetch the response.
        """
        prompt2 = prompt
        messages = [
            {"role": "system", "content": "You are a FashionFlow and users questions solver for perticular problem. read the below and if user ask any questions then solve it. description is 'Introducing our exquisite Gents Kurta designed to elevate your style for wedding occasions. Crafted with a keen eye for detail and tailored to perfection, this kurta embodies timeless elegance and cultural charm. Whether you're the groom, a family member, or a guest, this kurta is the epitome of grace and sophistication. Product Highlights: Design: Our Gents Kurta features a fusion of traditional and contemporary design elements, striking the perfect balance between classic and modern aesthetics. The intricate embroidery and embellishments add a regal touch, making it an ideal choice for weddings. Fabric: Carefully selected premium fabric ensures comfort throughout the celebrations. The fabric's rich texture and subtle shine enhance the overall look, making you stand out with every step. Color Palette: Available in a range of sophisticated colors, our kurta collection caters to various preferences and wedding themes. From deep royal hues to soft pastels, you'll find the perfect shade to complement the ambiance. Fit and Silhouette: The tailored fit offers a flattering silhouette, ensuring you look your best while maintaining ease of movement. The kurta's elegant drape exudes confidence and charm. Versatility: While perfect for weddings, our Gents Kurta also makes a versatile addition to your ethnic wardrobe. Pair it with churidar or trousers to create different looks for various occasions. Attention to Detail: Every stitch, button, and embellishment is a testament to our commitment to quality. The intricate patterns and delicate craftsmanship reflect the dedication that went into creating this masterpiece. Wear It With: Pair this Gents Kurta with traditional juttis or mojaris, and accessorize with a statement brooch or a stylish pocket square for added flair. Complete your look with a coordinating stole or dupatta to exude grandeur. Experience the Elegance: Our Gents Kurta for weddings captures the essence of celebration and cultural heritage. It's more than clothing; it's a piece of art that tells a story. Elevate your style and make a lasting impression on the most special occasions. Embrace the tradition, embody the style. Order your Gents Kurta for the wedding and make a statement that reflects your impeccable taste and appreciation for the finer things in life.'"},
            {"role": "user", "content": prompt2}
        ]

        try:
            async with ClientSession() as session:
                async with session.post(
                    "https://ava-alpha-api.codelink.io/api/chat",
                    headers={"Content-Type": "application/json"},
                    json={
                        "model": "gpt-4",
                        "temperature": 0.6,
                        "stream": True,
                        "messages": messages,
                    },
                    timeout=45,
                ) as resp_obj:
                    resp = ""
                    # print(resp_obj.headers)
                    async for line in resp_obj.content:
                        line_text = line.decode("utf-8").strip()
                        if line_text.startswith("data:"):
                            data = line_text.split("data:")[1]
                            try:
                                data_json = loads(data)
                                if "choices" in data_json:
                                    choices = data_json["choices"]
                                    for choice in choices:
                                        if (
                                            "finish_reason" in choice
                                            and choice["finish_reason"] == "stop"
                                        ):
                                            break
                                        if (
                                            "delta" in choice
                                            and "content" in choice["delta"]
                                        ):
                                            resp += choice["delta"]["content"]
                            except JSONDecodeError:
                                pass
                        messages.append({"role": "user", "content": prompt})
                        messages.append({"role": "assistant", "content": resp})
                    return resp
        except:
            raise Exception("Unable to fetch the response.")